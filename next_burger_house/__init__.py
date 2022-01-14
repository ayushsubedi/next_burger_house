from flask import Flask
from os import environ

application = Flask(__name__)


from next_burger_house import routes