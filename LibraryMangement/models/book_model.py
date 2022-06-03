from typing import List
from db import db


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'BookModel(id={self.id}, name={self.name}, publisher={self.publisher}, author={self.author})'

    @classmethod
    def find_by_id(cls, id) -> "BookModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["BookModel"]:
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
