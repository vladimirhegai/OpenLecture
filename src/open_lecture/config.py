from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="OPENLECTURE_", env_file=".env", extra="ignore")
    data_dir: Path = Path(".openlecture")
    max_upload_bytes: int = 100 * 1024 * 1024
    max_extracted_chars: int = 8_000_000
    api_token: str | None = None
    # Background AI reading and note generation (HTTP server only; MCP processes never run agents).
    agent_runner: bool = True

    @property
    def database(self) -> Path:
        return self.data_dir / "workspace.sqlite3"
