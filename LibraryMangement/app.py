from flask import Flask, jsonify
from marshmallow import ValidationError
from ma import ma
from namespaces import api
from db import db

app = Flask(__name__)

username = "root"
password = "abcdef"
server = "localhost:3306"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{server}/library_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


if __name__ == '__main__':
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
