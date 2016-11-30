from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:declanconn1@localhost/flaskInfo' # this is for logging into and connecting to the database
app.config['SECRET_KEY'] = 'super-secret' # this handles security provided by flask security
app.config['SECURITY_REGISTERABLE'] = True # this the register form
app.debug = True
db = SQLAlchemy(app)

# I got this code from Flask website for the database it was recommended to use for flask security. this is the website i got it from,http://pythonhosted.org//Flask-Security/quickstart.html#id1

# Define models creating the database
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile/<email>")
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first()
    return render_template("profile.html",  user=user)

@app.route("/post_user",methods=["POST"])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('HomePage'))




if __name__ == '__main__':
    app.run()
