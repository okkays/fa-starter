"""An example 'controller' with a basic route."""
from flask import Blueprint, redirect, url_for, current_app

blueprint = Blueprint('example', __name__)

@blueprint.route('/')
def index_real():
  return redirect(url_for('example.hello'))

@blueprint.route('/api/')
def index():
  return index_real()


@blueprint.route('/api/hello')
def hello():
  """Responds with hello.
  
  Returns:
    text string "hello"
  """
  return "hello"
