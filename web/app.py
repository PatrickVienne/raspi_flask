import flask_sqlalchemy
import flask
import os
import jinja2
import json
import git
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log',
                    level=logging.DEBUG)

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:my-secret-pw@mysqldb:3306/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)

class UsersPy(db.Model):

  __tablename__ = "userspy"

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String(255), nullable=False)

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def __repr__(self):
    return '<title {}'.format(self.username)


db.init_app(app)

db.create_all()
@app.route('/test_entry_db/')
def test_entry_db():
    admin = UsersPy('user1', 'password1')
    guest = UsersPy('user2', 'password2')

    db.session.add(admin)
    db.session.add(guest)

    #db.session.merge(admin)
    #db.session.merge(guest)
    db.session.commit()

    results = UsersPy.query.all()
    print(db.table)
    json_results = []
    for result in results:
      d = {'username': result.username,
           'password': result.password}
      json_results.append(d)

    return flask.jsonify(items=json_results)

@app.route('/testdb')
def testdb():
    #logging.info('Test Database query')
    print("testubg Database Connection")
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken.'



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
    app.run(debug=False, host='0.0.0.0', port=80, threaded=True)
