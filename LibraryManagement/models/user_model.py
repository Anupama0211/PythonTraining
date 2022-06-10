from sqlalchemy.exc import IntegrityError

from project.db import db
from typing import List

from exceptions.invalid_operation_exception import InvalidOperationException


class UserModel(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def add_books(self, books):
        self.books = books

    def __str__(self):
        return 'UsersModel(username=%s, name=%s,email=%s)' % (self.username, self.name, self.email)

    @classmethod
    def find_by_username(cls, username) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            raise InvalidOperationException("Email is already used!!")
