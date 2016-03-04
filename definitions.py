#!/usr/bin/python
import random 

# For representing the type of bet and it's associated odds
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

# Associates a bin on a roulette wheel with it's possible outcomes
# e.g. the '0' bin has outcomes of a straight bet on 0 or the five number 
# combination
# Here we want to extend (rather then wrap) the frozenset collection, since we
# can just keep all the base methods of the collection
class Bin(set):
    pass

# Selects the winning bin of a round
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

class BinBuilder():
    def __init__(self):

    def buildBins(self, wheel):
        # only straight bets so far
        for n in range(38):
            wheel.addOutcome(n, Outcome("straight bet", n))

# Used by the player to place an ammount on an outcome
class bets:
    pass

# A collection of bets placed on outcomes placed by player
class table:
    pass

# Employes a strategy to place an ammount of money on an outcome
class player:
    pass

# Runs the game - asks for bets, spins wheel, informs of wins/loses
class game:
    pass
