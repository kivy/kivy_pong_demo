import pytest
from pytest_trio.enable_trio_mode import \
    pytest_fixture_setup as trio_pytest_fixture_setup

from kivy.config import Config
Config.set('modules', 'touchring', '')

from pytest_kivy.app import AsyncUnitApp
from kivy_pong_demo.main import PongApp


class PongTestApp(AsyncUnitApp):

    app: PongApp


def pytest_fixture_setup(fixturedef, request):
    # unfortunately we can't parameterize fixtures from fixtures, so we have to
    # use a hammer to set window size and test class to use
    if fixturedef.argname == 'trio_kivy_app':
        request.param = {
            'kwargs': {'width': 1600, 'height': 900}, 'cls': PongTestApp}

    trio_pytest_fixture_setup(fixturedef, request)


@pytest.fixture
async def pong_app(trio_kivy_app) -> PongTestApp:
    try:
        await trio_kivy_app(PongApp)
        yield trio_kivy_app
    finally:
        if trio_kivy_app.app is not None:
            trio_kivy_app.app.clean_up()
