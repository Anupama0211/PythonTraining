from typing import List


from db import db


class LibraryModel(db.Model):
    __tablename__ = "library"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    book_id = db.Column(db.Integer, unique=True)

    def __init__(self, username, book_id):
        self.username = username
        self.book_id = book_id

    def __str__(self):
        return f'Library(id={self.id}, username={self.username}, book_id={self.book_id})'

    @classmethod
    def find_by_username(cls, username) -> "List[LibraryModel]":
        return cls.query.filter_by(username=username).all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
