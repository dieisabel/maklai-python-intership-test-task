import pathlib
import sys
import logging
from logging.config import dictConfig as configure_logging

from flask import Flask


def create_application():
    append_project_path()

    application = Flask(__name__)

    configure_application(application)

    with application.app_context():
        register_blueprints(application)
        register_shellcontext(application)

    return application


def configure_application(application):
    configure_logging(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                },
            },
        }
    )

    if application.debug:
        application.logger.setLevel(logging.DEBUG)
    else:
        application.logger.setLevel(logging.ERROR)


def register_blueprints(application):
    from api.controllers import blueprint

    application.register_blueprint(blueprint)


def register_shellcontext(application):
    def shellcontext():
        return {}

    application.shell_context_processor(shellcontext)


def append_project_path():
    PROJECT_DIR = pathlib.Path(__file__).resolve().parent.parent
    if str(PROJECT_DIR) not in sys.path:
        sys.path.append(str(PROJECT_DIR))
