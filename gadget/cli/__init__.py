from . import dev


def init(app):
    app.register_blueprint(dev.bp)
