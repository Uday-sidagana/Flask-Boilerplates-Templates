from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'
class User(db.Model):
    __tablename__='users'

    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email,password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def checkPassword(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'hi'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method =="POST":
        #handle resistration
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        new_user= User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login')) 

    return render_template('register.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method== "POST":
        email= request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.checkPassword(password):
            session['name'] = user.name
            session['email'] = user.email
            session['password'] = user.password

            return redirect(url_for('homepage'))
        else:
            return render_template('login.html', error= 'invalid user')


    return render_template('login.html')

@app.route('/homepage')
def homepage():
    if session['name']:
        user = User.query.filter_by(email=session['email']).first()

        return render_template('homepage.html', user= user)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)