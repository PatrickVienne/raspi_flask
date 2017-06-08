from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:my-secret-pw@192.168.0.88:3306/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

HTML="""<h1>Der Patrick ist geil. Shane ist aber MEGA Geil.</h1><p>Yippi</p><p>Connected?</p>kokoklkl"""


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
    print db.table
    json_results = []
    for result in results:
      d = {'username': result.username,
           'password': result.password}
      json_results.append(d)

    return jsonify(items=json_results)

@app.route('/testdb')
def testdb():
    #logging.info('Test Database query')
    print "testubg Database Connection"
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken.'


@app.route('/')
def hello_world():
    return HTML


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

