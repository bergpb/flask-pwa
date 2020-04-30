import pkg_resources
from os import environ
from flask import Flask, Blueprint, Markup, send_from_directory


class PWA(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.register_blueprint(app)
        app.add_url_rule("/sw.js", "serviceworker", self._init_sw)
        app.add_url_rule("/manifest.json", "manifest", self._init_manifest)
        app.add_url_rule("/offline", "offline", self._init_offline)

    def register_blueprint(self, app):
        app.register_blueprint(
            Blueprint(
                "pwa",
                __name__,
                static_url_path=app.static_url_path + "/pwa",
                static_folder="static",
                template_folder="templates",
            )
        )

    def _init_sw(self):
        return send_from_directory('static', 'js/sw.js')

    def _init_manifest(self):
        return send_from_directory('static', 'manifest.json')

    def _init_offline(self):
        return send_from_directory('templates', 'offline.html')
