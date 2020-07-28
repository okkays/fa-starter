"""An example 'controller' with a basic route."""
import os
import time

import flask
import logging
import requests

blueprint = flask.Blueprint('example', __name__, url_prefix="/example")


@blueprint.route("/ping")
def hello():
  return 'pong'
