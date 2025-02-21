from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='users'

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))




@app.route('/')
def index():
    return 'hi'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =="POST":
        #handle resistration
        pass
    return render_template('register.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method== "POST":
        pass
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)