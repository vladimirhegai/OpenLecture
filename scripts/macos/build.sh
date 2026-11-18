#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../.."
if [[ "$(uname -s)" != Darwin ]]; then
  echo 'Build this disk image on macOS.' >&2
  exit 1
fi

root="$(pwd -P)"
work="$(mktemp -d)"
work="$(cd "$work" && pwd -P)"
trap 'rm -rf "$work"' EXIT
stage="$work/stage"
app="$stage/Open Lecture.app"
contents="$app/Contents"
resources="$contents/Resources"
mkdir -p "$contents/MacOS" "$resources" "$root/dist/macos"

npm ci --prefix frontend
npm run build --prefix frontend
uv build --wheel --out-dir "$work/wheel"
uv export --locked --no-dev --no-emit-project --output-file "$work/requirements.txt" > /dev/null

uv python install --no-bin 3.12
python="$(uv python find --managed-python --no-project 3.12)"
runtime="$("$python" -I -c 'import sys; print(sys.base_prefix)')"
ditto "$runtime" "$resources/python"
python="$resources/python/bin/python3"
site_packages="$("$python" -I -c 'import sysconfig; print(sysconfig.get_path("purelib"))')"
case "$site_packages" in "$resources/python/"*) ;; *)
  printf 'The bundled interpreter resolved packages outside %s: %s\n' "$resources/python" "$site_packages" >&2
  exit 1
esac
uv pip install --python "$python" --target "$site_packages" --link-mode copy --require-hashes -r "$work/requirements.txt"
uv pip install --python "$python" --target "$site_packages" --link-mode copy --no-deps "$work"/wheel/*.whl
cp scripts/macos/serve.py LICENSE "$resources/"

version="$("$python" -I -c 'from importlib.metadata import version; print(version("open-lecture"))')"
cat > "$contents/Info.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key><string>OpenLecture</string>
    <key>CFBundleIdentifier</key><string>io.github.vladimirhegai.openlecture</string>
    <key>CFBundleName</key><string>Open Lecture</string>
    <key>CFBundleDisplayName</key><string>Open Lecture</string>
    <key>CFBundlePackageType</key><string>APPL</string>
    <key>CFBundleShortVersionString</key><string>$version</string>
    <key>CFBundleVersion</key><string>$version</string>
    <key>LSMinimumSystemVersion</key><string>14.0</string>
</dict>
</plist>
EOF

arch="$(uname -m)"
xcrun swiftc -swift-version 5 -O -target "$arch-apple-macosx14.0" scripts/macos/Launcher.swift -o "$contents/MacOS/OpenLecture"
codesign --force --sign - "$app"
codesign --verify --strict "$app"

ln -s /Applications "$stage/Applications"
image="$root/dist/macos/OpenLecture-$version-macos-$arch.dmg"
hdiutil create -quiet -ov -volname 'Open Lecture' -srcfolder "$stage" -format UDZO "$image"
hdiutil verify -quiet "$image"

mount="$work/mounted"
mkdir "$mount"
hdiutil attach -quiet -nobrowse -readonly -mountpoint "$mount" "$image"
trap 'hdiutil detach -quiet "$mount"; rm -rf "$work"' EXIT
resources="$mount/Open Lecture.app/Contents/Resources"
"$resources/python/bin/python3" -I -B "$root/scripts/macos/smoke.py" "$resources/serve.py" "$work/test-workspace"
echo "Built $image"
