import os

import flask
import flask_cors
from dotenv import load_dotenv

import example

load_dotenv()

# Set up the static folder to serve our angular client resources (*.js, *.css)
app = flask.Flask(__name__,
                  static_folder='dist/client', static_url_path='/client/')
app.register_blueprint(example.blueprint)

# If we're running in debug, defer to the typescript development server
# This gets us things like live reload and better sourcemaps.
if app.config['DEBUG']:
  app.config['API_URL'] = os.getenv('DEBUG_API_URL') or 'http://localhost:5000'
  app.config['ORIGIN'] = os.getenv('DEBUG_ORIGIN') or 'http://localhost:4200'

  flask_cors.CORS(app,
                  allow_headers='*',
                  origins=[app.config['ORIGIN']],
                  supports_credentials=True)
else:
  app.config['API_URL'] = os.getenv('PROD_API_URL')

# Set the secret key to enable access to session data.
app.secret_key = os.urandom(24)


# A catch-all route to serve the angular app.
# If no other routes match (such as /example) this will be called, and the
# angular app will take over routing.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_angular(path):
  if flask.current_app.config['DEBUG']:
    target = '/'.join([
      flask.current_app.config['ORIGIN'].rstrip('/'),
      app.static_url_path.strip('/'),
      path.lstrip('/')
    ])
    return flask.redirect(target)
  return flask.send_file('dist/client/index.html')
