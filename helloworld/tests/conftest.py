import flask
import pytest


@pytest.fixture(scope="module")
def app():
    return flask.Flask(__name__)


@pytest.fixture
def app_request():
    return flask.request
