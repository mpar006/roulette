from definitions import Outcome
from definitions import Bin
from definitions import Wheel
from definitions import BinBuilder
from definitions import Bet
from definitions import Table
import pytest

# Fixtures for Outcome tests
class Outcome_fixture:
   def __init__(self):
      self.o1 = Outcome("straight bet", 35)
      self.o2 = Outcome("straight bet", 35)
      self.o3 = Outcome("split bet", 17)
      self.o4 = Outcome("street bet", 11)

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

# Fixture for Wheel class tests
class Wheel_fixture:
   def __init__(self):
      self.w = Wheel()
      self.w.rng.seed(1)
      o = Outcome_fixture()
      self.w.addOutcome(5, o.o2)
      self.w.addOutcome(5, o.o3)
      self.w.addOutcome(5, o.o4)

@pytest.fixture()
def wheel_fixture(request):
   w = Wheel_fixture()
   return w

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

# Tests for wheel class
def test_add(wheel_fixture):
   assert len(wheel_fixture.w.get(5)) == 3

# next() in this case is deterministic, since we seeded the rng in the
# fixture
def test_next(wheel_fixture):
   assert len(wheel_fixture.w.next()) == 3
   assert len(wheel_fixture.w.next()) == 0

def test_map():
   w = Wheel()
   b = BinBuilder()
   b.buildBins(w)
   assert w.getOutcome("straight bet") == Outcome("straight bet", 35)
   assert w.getOutcome("split bet") == Outcome("split bet", 17)
   assert w.getOutcome("street bet") == Outcome("street bet", 11) 

# commented out since this is a manual check that requires looking at stdout
#def test_binBuild():
#   w = Wheel()
#   b = BinBuilder()
#   b.buildBins(w)
#   print w.get(1)

def test_winAmount(outcome_fixture):
   b = Bet(20, outcome_fixture.o1)
   assert b.winAmount() == 720

def test_looseAmount(outcome_fixture):
   b = Bet(20, outcome_fixture.o1)
   assert b.looseAmount() == 20

def test_table(outcome_fixture):
   t = Table()
   b = Bet(20, outcome_fixture.o1)
   t.placeBet(b)
   b = Bet(50, outcome_fixture.o3)
   t.placeBet(b)

   print t
