from flask import Blueprint


main_bp = Blueprint('main_page', __name__, template_folder='templates')

from . import views
from . import forms
from . import models