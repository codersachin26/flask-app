from flask import Flask
application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works!"

@application.route("/hello")
def hello():
    return "Hello Friend Again!!"


if __name__ == "__main__":
    application.run(debug=True)