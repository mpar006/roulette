from definitions import Outcome
from definitions import Bin
import pytest

# Fixtures for Outcome tests
class Outcome_fixture:
    def __init__(self):
        self.o1 = Outcome("straight bet", 35)
        self.o2 = Outcome("straight bet", 35)
        self.o3 = Outcome("split bet", 17)

@pytest.fixture()
def outcome_fixture(request):
    o = Outcome_fixture()
    return o

# Fixtures for Bin Class tests
class Bin_fixture:
    def __init__(self):
        self.five = Outcome("00-0-1-2-3", 6)
        self.zero = Bin([Outcome("0",35), self.five])

@pytest.fixture()
def bin_fixture(request):
    b = Bin_fixture()
    return b

# Tests for outcome class
def test_equal(outcome_fixture):
   assert outcome_fixture.o1 == outcome_fixture.o2

def test_notEqual(outcome_fixture):
   assert outcome_fixture.o1 != outcome_fixture.o3

def test_hash1(outcome_fixture):
   assert hash(outcome_fixture.o1) == hash(outcome_fixture.o2)

def test_hash2(outcome_fixture):
   assert hash(outcome_fixture.o1) != hash(outcome_fixture.o3)

def test_amount(outcome_fixture):
    assert outcome_fixture.o1.winAmount(10) == 350

# Tests for bin class
def test_len(bin_fixture):
    assert len(bin_fixture.zero) == 2

def test_ref(bin_fixture):
    zerozero = Bin([Outcome("00",35), bin_fixture.five])
    assert bin_fixture.zero.intersection(zerozero) == Bin([bin_fixture.five])
