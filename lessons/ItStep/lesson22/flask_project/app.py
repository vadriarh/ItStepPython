from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/home")
def welcome():
    return "Welcome to home!!!"

@app.route("/home/<name>")
def welcome_name(name):
    return f"Welcome to home, {name}!!!"

@app.route("/template/<name>")
def template(name):
    return render_template("index.html",name=name)

@app.route("/user")
def users():
    # people = ['Alice','Bob','Charlie']
    people = {
        'Alice':30,
        'Bob':25,
        'Charlie':35
    }
    return render_template('user.html',people=people)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4301,debug=True)