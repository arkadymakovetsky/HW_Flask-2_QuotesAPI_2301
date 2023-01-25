from api import db
from api.models.author import AuthorModel


class QuoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey(AuthorModel.id))
    text = db.Column(db.String(255), unique=False)
    rating = db.Column(db.Integer, default=1, server_default="0", nullable=False)

    def __init__(self, author: AuthorModel, text: str, rating: int = 1):
        self.author_id = author.id
        self.text = text
        self.rating = rating
