import os
import pkg_resources
from flask import Flask, Blueprint, Markup, send_file


class PWA(object):
    root_dir = os.path.dirname(os.getcwd())

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
        return send_file(
            pkg_resources.resource_stream("flask_pwa", "static/js/sw.js",),
            attachment_filename="sw.js",
        )

    def _init_manifest(self):
        return send_file(
            pkg_resources.resource_stream("flask_pwa", "static/manifest.json",),
            attachment_filename="manifest.json",
        )

    def _init_offline(self):
        return send_file(
            pkg_resources.resource_stream("flask_pwa", "templates/pwa/offline.html",),
            attachment_filename="offline.html",
        )
