from flask import Flask
from marshmallow import ValidationError

from exceptions.invalid_operation_exception import InvalidOperationException
from ma import ma
from middleware import init_middlewares
from namespaces import api
from db import db

app = Flask(__name__)

USERNAME = "root"
PASSWORD = "abcdef"
SERVER = "localhost:3306"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{SERVER}/library_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return {'message': error}, 400


@api.errorhandler(InvalidOperationException)
def handle_validation_error(error):
    return {'message': error.message}, 400


if __name__ == '__main__':
    init_middlewares(app)
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
