from db import db
from typing import List


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __init__(self, id, name, publisher, author, ):
        self.id = id
        self.name = name
        self.publisher = publisher
        self.author = author

    def __repr__(self):
        return 'BookModel(id=%sd, name=%s, publisher=%s, author=%s)' % (self.id, self.name, self.publisher, self.author)

    def json(self):
        return {'id': self.id, 'name': self.name, 'publisher': self.publisher, 'author': self.author}

    @classmethod
    def find_by_id(cls, id) -> "BookModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["BookModel"]:
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

