from flask import Flask


def create_application():
    application = Flask(__name__)

    with application.app_context():
        register_blueprints(application)

        if application.debug:
            register_shellcontext(application)

    return application


def register_blueprints(application):
    from controllers import blueprint

    application.register_blueprint(blueprint)


def register_shellcontext(application):
    def shellcontext():
        return {}

    application.shell_context_processor(shellcontext)
