import "katex/dist/katex.min.css";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import { Toasts } from "./components/ui";
import "./styles.css";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Toasts>
      <App />
    </Toasts>
  </StrictMode>,
);
