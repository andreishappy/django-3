from dataclasses import dataclass
import os


@dataclass
class Environment:
    SECRET_KEY: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str


def get_environment_variable(*, key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise Exception(f"Environment variable missing: {key}")
    return value


environment = Environment(
    SECRET_KEY=get_environment_variable(key="SECRET_KEY"),
    POSTGRES_USER=get_environment_variable(key="POSTGRES_USER"),
    POSTGRES_PASSWORD=get_environment_variable(key="POSTGRES_PASSWORD"),
    POSTGRES_DB=get_environment_variable(key="POSTGRES_DB"),
    POSTGRES_HOST=get_environment_variable(key="POSTGRES_HOST"),
    POSTGRES_PORT=get_environment_variable(key="POSTGRES_PORT"),
)
