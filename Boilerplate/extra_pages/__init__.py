from flask import Blueprint

extra= Blueprint('extra', __name__, template_folder='templates')

from extra_pages import routes