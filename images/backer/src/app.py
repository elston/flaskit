import traceback

from flask import (
    Flask, 
    render_template)

from flask_uploads import (
    configure_uploads,  
    patch_request_class)

from extensions import (
    config,
    bcrypt, 
    csrf_protect, 
    db, 
    login_manager,
    migrate,
    webpack
)



def register_extensions(app):

    # ..config
    config.init_app(app)

    # ..bcrypt
    bcrypt.init_app(app)

    # ..db
    db.init_app(app)

    # ..csrf
    csrf_protect.init_app(app)

    # ...login_manager
    login_manager.init_app(app)
    login_manager.login_view = 'accounts.login'
    login_manager.login_message = None

    @login_manager.user_loader
    def load_user(user_id):
        from accounts.models import User
        return User.get_by_id(user_id)

    # ..migrate
    migrate.init_app(app, db)

    # ..webpack    
    if not app.config['MIGRATION_MODE']:
        webpack.init_app(app)
    
    # ...
    return None


# ...blueprints
from lending import views as lending_views
from accounts import views as accounts_views
# ...
def register_blueprints(app):
    # ..
    app.register_blueprint(lending_views.blueprint)
    app.register_blueprint(accounts_views.blueprint)
    # ..
    return None


def register_errorhandlers(app):

    # ..
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code

    # ..
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)

    # ..
    return None


# ...models
from accounts import models as accounts_models
# ...
def register_shellcontext(app):

    # ...
    def shell_context():
        return {
            'db': db,
            'User': accounts_models.User,
        }

    # ...
    app.shell_context_processor(shell_context)


# ..commands
import commands
# ..
def register_commands(app):
    # ..
    app.cli.add_command(commands.createadmin)


def create_app():
    # ..
    app = Flask(__name__.split('.')[0])
    # ...
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    # ..
    return app

app = create_app()
# print(app.url_map)