from bbquote.lib import get_quote

def test_quote():
    result = get_quote()
    assert len(result) != 0
