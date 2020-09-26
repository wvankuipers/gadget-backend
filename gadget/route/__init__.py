from . import default, api


def init(app):
    app.register_blueprint(default.bp)

    api.init(app)
