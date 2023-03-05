from . import main_bp
from ..utils.utils import parse_cookie, del_cookie

from flask import render_template, request, make_response


@main_bp.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    cookie = request.cookies.get('notes') 
    notes_cookie = cookie if cookie else ''
    
    if request.method == 'POST':
        note_id = request.form['noteId']
        note_val = request.form['noteVal']
        
        notes_cookie += f'{note_id}:{note_val};'
        resp = make_response(render_template('main_page/index.html'))
        resp.set_cookie("notes", notes_cookie)
        
        return resp
    elif request.method == 'DELETE':
        note_id = request.form['noteId']
        
        notes_cookie = del_cookie(notes_cookie, note_id)
        resp = make_response(render_template('main_page/index.html'))
        resp.set_cookie("notes", notes_cookie)
        
        return resp
    notes = parse_cookie(notes_cookie)
    
    return render_template('main_page/index.html', notes=notes)