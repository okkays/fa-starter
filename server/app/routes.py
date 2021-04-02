"""An example 'controller' with a basic route."""
from flask import Blueprint, redirect, url_for, current_app

blueprint = Blueprint('example', __name__)

@blueprint.route('/')
def index():
  return redirect(url_for('example.hello'))


@blueprint.route('/hello')
def hello():
  """Responds with hello.
  
  Returns:
    text string "hello"
  """
  return "hello"
