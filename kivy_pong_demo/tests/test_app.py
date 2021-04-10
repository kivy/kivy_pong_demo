

async def test_open_app(pong_app):
    await pong_app.wait_clock_frames(5)


async def test_app_settings(pong_app):
    assert pong_app.app.root.ids.player_left.score >= 0
    assert pong_app.app.root.ids.player_right.score >= 0
