from pathlib import Path
import tomllib


DEFAULT_CONFIG_PATH = Path("config.toml")


def load_config(path: Path = DEFAULT_CONFIG_PATH) -> dict:
    """
    Load application configuration from a TOML file.
    """
    if not path.exists():
        return {}

    with path.open("rb") as config_file:
        return tomllib.load(config_file)
