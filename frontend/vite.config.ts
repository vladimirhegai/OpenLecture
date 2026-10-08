import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

const api = process.env.OPENLECTURE_API ?? "http://127.0.0.1:8000";

export default defineConfig({
  plugins: [react()],
  build: { outDir: "../src/open_lecture/web", emptyOutDir: true, chunkSizeWarningLimit: 1500 },
  server: {
    proxy: {
      "/api": {
        target: api,
        changeOrigin: true,
        // The backend rejects cross-origin writes; the dev proxy is same-origin by construction.
        configure: (proxy) => proxy.on("proxyReq", (request) => request.removeHeader("origin")),
      },
    },
  },
});
