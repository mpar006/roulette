from outcome import Outcome

def test_equal():
    o1 = Outcome("straight bet", 35)
    o2 = Outcome("straight bet", 35)
    o3 = Outcome("split bet", 17)
    assert o1 == o2

def test_notEqual():
    o1 = Outcome("straight bet", 35)
    o2 = Outcome("split bet", 17)
    assert o1 != o2

def test_hash1():
    o1 = Outcome("straight bet", 35)
    o2 = Outcome("straight bet", 35)
    assert hash(o1) == hash(o2)

def test_hash2():
    o1 = Outcome("straight bet", 35)
    o2 = Outcome("split bet", 17)
    assert hash(o1) != hash(o2)

def test_amount():
    o1 = Outcome("straight bet", 35)
    assert o1.winAmount(10) == 350
