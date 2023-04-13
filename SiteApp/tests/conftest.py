import pytest
from SiteApp import create_app
from SiteApp import db as _db
from SiteApp.config import TestingConfig
from .factories import OrderDriverFactory, OrderConductorFactory


@pytest.fixture(scope='session')
def app():
    _app = create_app(TestingConfig)

    with _app.app_context():
        _db.create_all()

    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture()
def test_app(app):
    """ Returns app for tests """
    return app.test_client()


@pytest.fixture(scope='session')
def db(app):
    """ DB for tests """
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Cleaning the db
    _db.session.close()
    _db.drop_all()


@pytest.fixture(scope='session')
def order_driver(db):
    order_d = OrderDriverFactory()
    db.session.add(order_d)
    db.session.commit()
    return order_d


@pytest.fixture(scope='session')
def order_conductor(db):
    order_c = OrderConductorFactory()
    db.session.add(order_c)
    db.session.commit()
    return order_c
