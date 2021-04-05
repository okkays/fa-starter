"""Primary module for the flask app"""
import os
from flask import Flask
from app import api

def create_app(config=None):
  """Configure and create flask app.

  Returns:
    flask app
  """
  app = Flask(__name__)
  env_cfg = os.environ.get('APP_SETTINGS')
  if config:
    app.config.from_object(config)
  elif env_cfg:
    app.config.from_object(env_cfg)
  else:
    app.config.from_object('app.config.ProdConfig')
  app.register_blueprint(api.blueprint)
  return app