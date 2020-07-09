from flask import Flask, render_template, request, redirect, url_for
from models.user import Db, User
from modules.userform import UserForm

app = Flask(__name__)

# connectin database to app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "s14a-key"
Db.init_app(app)


@app.route('/')
def index():
    # Query all
    users = User.query.all()

    # Iterate and print
    for user in users:
        User.toString(user)

    return render_template("index.html")
