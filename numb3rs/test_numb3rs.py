from numb3rs import validate


def test_value_false():
    assert validate("277.400.100.2") == False
    assert validate("1.400.2.300") == False


def test_value_true():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True

