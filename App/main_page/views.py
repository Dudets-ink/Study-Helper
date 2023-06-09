from . import main_bp
from ..models import Notes
from .. import db

from flask import render_template, request
from flask_login import current_user


@main_bp.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    """Renders index page.
    Handles such methods as:
    GET - page entry, loading array of notes from DB
    POST - adds note, puts note to DB and conjoin with user
    DELETE - delete note form DB

    Returns:
        Html main page
    """
    if request.method == 'POST':
        note_val = request.form['noteVal']
        
        note = Notes(user_id=current_user.id, text=note_val)
        db.session.add(note)
        db.session.commit()
    elif request.method == 'DELETE':
        note_id = request.form['noteId']
        note = Notes.query.filter_by(id=note_id).first()
        
        db.session.delete(note)
        db.session.commit()
    notes = Notes.query.filter_by(user_id=current_user.id).all() \
            if current_user.is_authenticated else ''
    
    return render_template('index.html', notes=notes)
