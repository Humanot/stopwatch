import pytest
from fixture.application import Application

fixture=None

@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    return fixture

@pytest.fixture (scope="session", autouse=True)
def stop(request):
    def in_out():
        fixture.destroy()
    request.addfinalizer(in_out)