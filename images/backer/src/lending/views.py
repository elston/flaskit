from flask import Blueprint, render_template
from flask import current_app as app


blueprint = Blueprint('lending', __name__, 
    url_prefix=''
)


@blueprint.route('/')
def index():
    login_url = app.config.get('LOGIN_URL')
    return render_template('lending/index.html', 
        login_url = login_url, 
    )    

@blueprint.route('/eggs')
def eggs():
    login_url = app.config.get('LOGIN_URL')
    return render_template('lending/eggs.html', 
        login_url = login_url, 
    )       