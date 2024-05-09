from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"


def test_shorten_uppercase():
    assert shorten("Message") == "Mssg"
    assert shorten("Calculator") == "Clcltr"


def test_shorten_numbers():
    assert shorten("num 123") == "nm 123"

def test_shorten_vowel():
    assert shorten("Oyster") == "ystr"
    assert shorten("Ambassador") == "mbssdr"

def test_shorten_punct():
    assert shorten("hello, friend") == "hll, frnd"

