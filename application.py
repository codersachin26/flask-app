from flask import Flask
application = Flask(__name__)

@application.route("/")
def index():
    return "Hello Friends Again!!!"



if __name__ == "__main__":
    application.run(debug=True)