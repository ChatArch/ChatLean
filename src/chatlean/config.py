"Typed environment configuration for ChatLean."

from chatenv import BaseEnvConfig, EnvField


class ChatleanConfig(BaseEnvConfig):
    "ChatLean ChatEnv configuration."

    _title = "ChatLean Configuration"
    _aliases = ["chatlean"]
    _storage_dir = "Chatlean"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATLEAN_API_KEY = EnvField(
        "CHATLEAN_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatleanConfig"]
