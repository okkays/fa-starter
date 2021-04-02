"""Flask configuration."""
import os

class Config:
    """Base config."""
    EXAMPLEVAR = os.environ.get("EXAMPLEVAR")
class DevConfig(Config):
    """Dev config."""
    SECRET_KEY="my_dev_session_key"
class ProdConfig(Config):
    """Prod/Default Config."""
    SECRET_KEY=os.urandom(24)