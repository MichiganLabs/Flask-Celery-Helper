from flask import current_app
import pytest

from flask.ext.celery import Celery


class FakeApp(object):
    config = dict(REDIS_URL='redis://localhost')
    static_url_path = ''
    import_name = ''

    def register_blueprint(self, _):
        pass


def test_multiple():
    assert 'celery' in current_app.extensions

    with pytest.raises(ValueError):
        Celery(current_app)


def test_one_dumb_line():
    app = FakeApp()
    Celery(app)
    assert 'celery' in app.extensions
