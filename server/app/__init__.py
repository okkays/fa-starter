"""Primary module for the flask app"""
import os
from flask import Flask
from app import routes

def create_app(config='app.config.ProdConfig'):
  """Configure and create flask app.

  Returns:
    flask app
  """
  app = Flask(__name__)
  app.config.from_object(config)
  override = os.environ.get('APP_SETTINGS')
  app.config.from_object(override)
  app.register_blueprint(routes.blueprint)
  return app