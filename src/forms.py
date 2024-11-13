from flask import Blueprint, render_template , redirect, url_for, request
from . import db
from .models import Photo
from typing import Optional,List

form_bp = Blueprint('form_bp', __name__)

@form_bp.route('/')
def index():
    photos: List[Photo] = Photo.query.all()
    return render_template('index.html', photos=photos)

@form_bp.route('/add', methods=['POST','GET'])
def add() -> Optional[str]:
    if request.method == 'POST':
        title : str= request.form.get('title')
        description : str=request.form.get('description')
        image_url : str = request.form.get('image_url')

        if not title or not image_url:
            return "No pueden quedar vacios el titulo y la imagen", 400
    
        new_photo = Photo (title=title, description=description, image_url=image_url)
        db.session.add(new_photo)
        db.session.commit()
        return redirect(url_for('form_bp.index'))
    return render_template('photo_form.html')