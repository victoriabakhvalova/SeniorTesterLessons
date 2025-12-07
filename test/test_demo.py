import pytest

@pytest.fixture()
def before_after():
    print("precondition for a test")
    yield None
    print("\nthis is for after test")


def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 4

