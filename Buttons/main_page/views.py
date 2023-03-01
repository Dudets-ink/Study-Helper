from . import main_bp

from flask import render_template, request

from Buttons import cache


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print('\n\n\n\n\n\nLOOOL')
        print(request.form['sdf'])
    
    return render_template('main_page/index.html')