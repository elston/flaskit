# ..
from config import Config
config = Config()

# ..
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# ..
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# ..
from flask_wtf.csrf import CSRFProtect
csrf_protect = CSRFProtect()

# ..
from flask_login import LoginManager
login_manager = LoginManager()

# ..
from flask_migrate import Migrate
migrate = Migrate()

# ..
from libs.flask_webpack import Webpack
webpack = Webpack()