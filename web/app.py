import flask_sqlalchemy
import flask
import os
import jinja2
import json
import git
import logging
from OpenSSL import SSL

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('domain.key')
context.use_certificate_file('domain.crt')


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log',
                    level=logging.DEBUG)

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

app = flask.Flask(__name__)

@app.before_first_request
def setup_logging():
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)


@app.route('/')
def hello_world():
    logging.info("received request")
    template = jinja_env.get_template("index.html")
    params = {}
    return template.render(params)


@app.route('/GITHUBHOOK', methods=['POST'])
def on_push():
    project_dir = os.path.dirname(os.getcwd())
    git.Repo.init(project_dir)
    repo = git.Repo(project_dir)
    origin = repo.create_remote('origin', 'https://github.com/PatrickVienne/raspi_flask')
    logging.debug('Identified Repo in: {}'.format(project_dir))
    #origin = repo.create_remote('origin', repo.remotes.origin.url)
    logging.debug('Created repo origin with url: {}'.format(repo.remotes.origin.url))
    logging.debug('Pulling from remote: {}'.format(repo.remotes.origin.url))
    origin.pull()
    logging.debug('Finished pulling: {}'.format(repo.remotes.origin.url))
    #logging.debug('{}'.format(flask.request.__dict__))
    #logging.debug('{}'.format(flask.request.get_json()))
    logging.debug('Remote Pushed: {}'.format(flask.request.get_json().get('url')))
    logging.debug('Remote Branch Pushed: {}'.format(flask.request.get_json().get('master_branch')))
    return flask.make_response()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80, threaded=True, ssl_context=context)
