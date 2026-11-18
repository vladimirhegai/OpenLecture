import AppKit

final class Launcher: NSObject, NSApplicationDelegate {
    private var server: Process?
    private var output: FileHandle?
    private var address: URL?
    private var logURL: URL?
    private var quitting = false

    func applicationDidFinishLaunching(_ notification: Notification) {
        let menu = NSMenu()
        let appItem = NSMenuItem()
        let appMenu = NSMenu(title: "Open Lecture")
        appMenu.addItem(withTitle: "Open in Browser", action: #selector(openInBrowser), keyEquivalent: "o").target = self
        appMenu.addItem(.separator())
        appMenu.addItem(withTitle: "Quit Open Lecture", action: #selector(NSApplication.terminate(_:)), keyEquivalent: "q")
        appItem.submenu = appMenu
        menu.addItem(appItem)
        NSApp.mainMenu = menu

        do {
            try startServer()
        } catch {
            showError(error.localizedDescription)
        }
    }

    private func startServer() throws {
        let files = FileManager.default
        let data = try files.url(for: .applicationSupportDirectory, in: .userDomainMask,
                                 appropriateFor: nil, create: true).appendingPathComponent("Open Lecture")
        try files.createDirectory(at: data, withIntermediateDirectories: true)
        let log = data.appendingPathComponent("server.log")
        logURL = log
        try Data().write(to: log)

        let resources = Bundle.main.resourceURL!
        let process = Process()
        process.executableURL = resources.appendingPathComponent("python/bin/python3")
        process.arguments = ["-I", "-B", resources.appendingPathComponent("serve.py").path]
        process.currentDirectoryURL = data
        var environment = ProcessInfo.processInfo.environment
        environment["OPENLECTURE_DATA_DIR"] = data.path
        let localBin = files.homeDirectoryForCurrentUser.appendingPathComponent(".local/bin").path
        environment["PATH"] = [localBin, "/opt/homebrew/bin", "/usr/local/bin", environment["PATH"] ?? "/usr/bin:/bin"]
            .joined(separator: ":")
        process.environment = environment
        process.standardInput = FileHandle.nullDevice
        let pipe = Pipe()
        process.standardOutput = pipe
        process.standardError = try FileHandle(forWritingTo: log)
        process.terminationHandler = { [weak self] _ in
            DispatchQueue.main.async { self?.serverStopped() }
        }
        try process.run()
        server = process
        output = pipe.fileHandleForReading
        // The backend prints its address once startup is complete, then keeps stdout open.
        NotificationCenter.default.addObserver(self, selector: #selector(serverReady(_:)),
                                               name: .NSFileHandleDataAvailable, object: output)
        output?.waitForDataInBackgroundAndNotify()
    }

    @objc private func serverReady(_ notification: Notification) {
        guard let output = notification.object as? FileHandle else { return }
        NotificationCenter.default.removeObserver(self, name: .NSFileHandleDataAvailable, object: output)
        let line = String(decoding: output.availableData, as: UTF8.self).trimmingCharacters(in: .whitespacesAndNewlines)
        guard let url = URL(string: line), url.host == "127.0.0.1", url.port != nil else { return }
        address = url
        openInBrowser()
    }

    @objc private func openInBrowser() {
        if let address { NSWorkspace.shared.open(address) }
    }

    func applicationShouldHandleReopen(_ sender: NSApplication, hasVisibleWindows flag: Bool) -> Bool {
        openInBrowser()
        return false
    }

    private func serverStopped() {
        if quitting {
            NSApp.reply(toApplicationShouldTerminate: true)
        } else {
            showError("Open Lecture's local server stopped.")
        }
    }

    private func showError(_ message: String) {
        NSApp.activate(ignoringOtherApps: true)
        let alert = NSAlert()
        alert.alertStyle = .critical
        alert.messageText = "Open Lecture could not start"
        alert.informativeText = [message, logURL.map { "Server log: \($0.path)" }].compactMap { $0 }.joined(separator: "\n\n")
        alert.runModal()
        NSApp.terminate(nil)
    }

    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply {
        guard let server, server.isRunning else { return .terminateNow }
        quitting = true
        server.terminate()
        return .terminateLater
    }
}

let app = NSApplication.shared
let launcher = Launcher()
app.setActivationPolicy(.regular)
app.delegate = launcher
app.run()
