import pytest

from factory import create_application


@pytest.fixture()
def application():
    app = create_application()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(application):
    return application.test_client()
