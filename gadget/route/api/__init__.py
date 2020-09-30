from . import project, suite, run, test


def init(app):
    API_BASE = f"/api/v{app.config['API_VERSION']}"

    app.register_blueprint(project.bp, url_prefix=f"{API_BASE}/project")
    app.register_blueprint(suite.bp, url_prefix=f"{API_BASE}/suite")
    app.register_blueprint(run.bp, url_prefix=f"{API_BASE}/run")
    app.register_blueprint(test.bp, url_prefix=f"{API_BASE}/test")
