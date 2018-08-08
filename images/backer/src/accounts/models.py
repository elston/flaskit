import datetime as dt
from flask_login import UserMixin

from database import Column, Model, SurrogatePK, db, reference_col, relationship
from extensions import bcrypt


class User(UserMixin, SurrogatePK, Model):

    __tablename__ = 'users'

    username = Column(db.String(80), unique=True, nullable=False) #..email
    password = Column(db.Binary(128), nullable=True)

    # ..
    created = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    is_active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)    


    def __init__(self, username, password=None, **kwargs):
        # ..
        Model.__init__(self, username=username, password=password, **kwargs)

        # ..
        if password:
            self.set_password(password)
        else:
            self.password = None

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)    