from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello Hazem Ben Salem , you are the best developer on the planet!'
