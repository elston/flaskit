from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length

from .models import User


class LoginForm(FlaskForm):

    username = StringField('Username',
        validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password',
        validators=[DataRequired(), Length(min=6, max=40)])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None


    def validate(self):
        # ...
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append('Unknown username')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        return True        