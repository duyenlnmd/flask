from flask import Flask
from flask import Flask, render_template

app = Flask("Demo")

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/user")
def user():
    return "Hi Duyen!"

if __name__ == "__main__":
    app.run()

