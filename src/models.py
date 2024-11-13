
from flask_sqlalchemy import SQLAlchemy
from typing import Optional
from . import db

class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description: Optional[str] = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"<Photo {self.title}>"
