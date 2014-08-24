import bender_futurama_quotes


def test_hello(bender_tester):
    m = bender_tester.user_send('quote')
    assert m.replies[0] in bender_futurama_quotes.QUOTES
