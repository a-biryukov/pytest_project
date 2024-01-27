from utils.dicts import get_val


def test_get_val():
    assert get_val({"1": "elefant", "2": "fox", "3": "mouse"}, "1") == "elefant"
    assert get_val({"1": "elefant", "2": "fox", "3": "mouse"}, "4") == "unicorn"
    assert get_val({}, "1", "fish") == "fish"

