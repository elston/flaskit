from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from utils import flash_errors

blueprint = Blueprint('accounts', __name__, 
    url_prefix='/accounts'
)

from .forms import LoginForm

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # ..
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            redirect_url = request.args.get('next') or url_for('admin.index')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    # ..
    return render_template('accounts/login.html', form=form)    


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('admin.index'))    