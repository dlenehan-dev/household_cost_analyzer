# household_cost_analyzer/config.py

from dataclasses import dataclass
from pathlib import Path
import tomllib

DEFAULT_CONFIG_PATH = Path("config.toml")


@dataclass(frozen=True)
class Config:
    logging: dict
    currency_symbol: str


def load_config(path: Path = DEFAULT_CONFIG_PATH) -> Config:
    with path.open("rb") as f:
        data = tomllib.load(f)

    return Config(
        logging=data["logging"],
        currency_symbol=data["reporting"]["currency_symbol"],
    )
