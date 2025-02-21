from flask import Blueprint

extra= Blueprint('extra', __name__)

from extra_pages import routes