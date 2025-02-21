from flask import Flask, request, render_template

app = Flask(__name__)

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