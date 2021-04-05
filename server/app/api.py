"""An example 'controller' with a basic route."""
from flask import Blueprint, redirect, url_for, current_app

blueprint = Blueprint('api', __name__)

@blueprint.route('/')
def index_real():
  return redirect(url_for('api.example'))

@blueprint.route('/api/')
def index():
  return index_real()


@blueprint.route('/api/example')
def example():
  """Responds with hello.
  
  Returns:
    text string "hello"
  """
  return "hello"
