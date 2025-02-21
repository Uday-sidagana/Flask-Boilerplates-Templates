from extra_pages import extra
from flask import render_template

@extra.route('/extra')
def extra():
    return render_template('index.html')
