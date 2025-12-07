from dataclasses import dataclass, field
from environs import Env


@dataclass
class Config:
    host: str = field(repr=True, default='localhost')
    port: int = field(repr=True, default=8000)


def load_config() -> Config:
    env = Env()
    env.read_env()
    return Config(
        host=env("API_HOST"),
        port=int(env("API_PORT"))
    )
