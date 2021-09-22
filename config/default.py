from pydantic import BaseSettings


class Setting(BaseSettings):
    db_name: str = None
    db_host: str = 'host.docker.internal'
    db_port: int = 27017

    class Config:
        env_file = '.env'


config = Setting()