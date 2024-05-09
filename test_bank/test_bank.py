from bank import value

def test_value_zero():
    assert value("hello") == "$0"
    assert value("hello, friend") == "$0"
    # assert value("Hello world") == "$0"
    # assert value("simooon") == "$0"
    # assert value("What's up") == "$0"

def test_value_20():
    assert value("hola") == "$20"
    assert value("hamood") == "$20"
    assert value("hay") == "$20"

def test_value_100():
    assert value("Tanjula Chemi Saxeli Brat") == "$100"
    assert value("tanjula chemi saxeli brat") == "$100"
    assert value("subariki simooon") == "$100"
    # assert value("hello") == "$100"

def test_value_num():
    assert value("555") == "$100"

