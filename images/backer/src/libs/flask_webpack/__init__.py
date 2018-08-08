import json
from flask import current_app


class Webpack(object):
    def __init__(self, app=None):
        # ...
        self.app = app

        if app is not None:
            self.init_app(app)


    def init_app(self, app):

        # Setup a few sane defaults.
        app.config.setdefault('WEBPACK_MANIFEST_PATH',
                              '/tmp/themostridiculousimpossiblepathtonotexist')
        app.config.setdefault('WEBPACK_ASSETS_URL', '/')

        # ..
        self._set_asset_paths(app)

        # ...
        if app.config.get('DEBUG', False):
            app.before_request(self._refresh_webpack_stats)

        # ...
        app.add_template_global(self.asset_url_for)


    def _set_asset_paths(self, app):

        # ..
        webpack_stats = app.config['WEBPACK_MANIFEST_PATH']
        # ..
        try:
            with app.open_resource(webpack_stats, 'r') as stats_json:
                # ..
                stats = json.load(stats_json)
                # ..
                self.assets = stats
                self.assets_url = app.config['WEBPACK_ASSETS_URL']

        except IOError:
            raise RuntimeError(
                "Flask-Webpack requires 'WEBPACK_MANIFEST_PATH' "
                " to be set and it must point to a valid json file.")


    def _refresh_webpack_stats(self):
        # ..
        self._set_asset_paths(current_app)


    def asset_url_for(self, asset):
        # ..
        if asset not in self.assets:
            return None
        # ..
        return '{0}/{1}'.format(self.assets_url, self.assets[asset])
