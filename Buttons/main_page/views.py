from . import main_bp
from flask import render_template


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main_page/index.html')