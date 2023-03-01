from . import main_bp
from ..utils.utils import parse_cookie

from flask import render_template, request, make_response


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    cookies = request.cookies.get('notes') 
    notes = cookies if cookies else ''
    
    if request.method == 'POST':
        note_id = request.form['noteId']
        note_val = request.form['noteVal']
        
        notes += f'{note_id}:{note_val};'
        resp = make_response(render_template('main_page/index.html'))
        resp.set_cookie("notes", notes)
        
        return resp
    notes = parse_cookie(notes)
    
    return render_template('main_page/index.html', notes=notes)