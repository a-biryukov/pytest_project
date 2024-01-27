from utils import arrs


def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 2) == [2]
    assert arrs.my_slice(array_fixture, 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(array_fixture, None) == [1, 2, 3]
