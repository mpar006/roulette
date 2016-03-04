#!/usr/bin/python
import random 

class Outcome:
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def winAmount(self, amount):
        return self.odds * amount

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return "{} ({}:1)".format(self.name, self.odds)

    def __repr__(self):
        return "Outcome({}, {}".format(self.name, self.odds)

# Here we want to extend (rather then wrap) the frozenset collection, since we
# can just keep all the base methods of the collection
class Bin(set):
    pass

class Wheel:
    def __init__(self):
        self.bins = tuple(Bin() for i in range(38))
        self.rng = random.Random()

    def addOutcome(self, number, outcome):
        self.bins[number].add(outcome)

    def next(self):
        return self.rng.choice(self.bins)

    def get(self, bin):
        return self.bins[bin]
