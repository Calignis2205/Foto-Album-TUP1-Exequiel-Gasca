from flask import Blueprint, render_template , redirect, url_for, request
from .models import db, Photo
from typing import List

photo_bp = Blueprint('photo_bp',__name__)

@photo_bp.route('/photo')
def index():
    photos: List[Photo] = Photo.query.all()
    return render_template('index.html', photos=photos)

@photo_bp.route('/delete/<int:id>', methods=['POST','GET'])
def delete(id: int) -> str:
    photo : Photo = Photo.query.get(id)
    db.session.delete(photo)
    db.session.commit()
    return redirect(url_for('photo_bp.index'))

@photo_bp.route('/update/<int:id>', methods=['POST','GET'])
def update(id: int) -> str:
    photo : Photo = Photo.query.get(id)
    if request.method == 'POST':
        photo.title = request.form['title']
        photo.description = request.form['description']
        photo.image_url = request.form['image_url']

        if not photo.title or not photo.image_url:
            return 'No pueden quedar vacios el titulo y la imagen', 400
    
        db.session.commit()
        return redirect(url_for('photo_bp.index'))
    
    return render_template('photo_form.html', photo=photo)
