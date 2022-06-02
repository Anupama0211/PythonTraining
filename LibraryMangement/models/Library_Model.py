from db import db
from typing import List


class LibraryModel(db.Model):
    __tablename__ = "library"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    book_id = db.Column(db.Integer)

    def __init__(self, id, username,book_id):
        self.id = id
        self.username = username
        self.book_id=book_id

    def __repr__(self):
        return 'Library(id=%d, username=%s, book_id=%d)' % (self.id, self.username, self.book_id)

    def json(self):
        return {'id': self.id, 'username': self.username, 'book_id':self.book_id}

    @classmethod
    def find_by_username(cls, username) -> "LibraryModel":
        return cls.query.filter_by(username=username).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
