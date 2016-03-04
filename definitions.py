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
        straightBet(wheel)
        streetBet(wheel)
        lineBet(wheel)
        dozenBet(wheel)

    def straightBet(self, wheel):
        for n in range(38):
            wheel.addOutcome(n, Outcome("straight bet", 35))
    
    def horizontalSplitBet(self, wheel):
        for r in range(11):
            n = 3 * r + 1
            o = Outcome("split bet", 17)
            wheel.addOutcome(n, o)
            wheel.addOutcome(n + 1, o)
            n = 3 * r + 2
            wheel.addOutcome(n, o)
            wheel.addOutcome(n + 1, o)

    def verticalSplitBet(self, wheel):
        for n in range(1,34):
            o = Outcome("split bet", 17)
            wheel.addOutcome(n, o)
            wheel.addOutcome(n + 3, o)

    def streetBet(self, wheel):
        for r in range(11):
            n = 3 * r + 1
            o = Outcome("street bet", 11)
            wheel.addOutcome(n, o)
            wheel.addOutcome(n + 1, o)
            wheel.addOutcome(n + 2, o)

    def cornerBet(self, wheel):
        for r in range(10):
            n = 3 * r + 1
            o = Outcome("corner bet", 8)
            wheel.addOutcome(n, o)
            wheel.addOutcome(n + 1, o)
            wheel.addOutcome(n + 3, o)
            wheel.addOutcome(n + 4, o)
            n = 3 * r + 2
            wheel.addOutcome(n, o)
            wheel.addOutcome(n + 1, o)
            wheel.addOutcome(n + 3, o)
            wheel.addOutcome(n + 4, o)


    def lineBet(self, wheel):
        for r in range(10):
            n = 3 * r + 1
            o = Outcome("line bet", 5)
            wheel.addOutcome(n, o)
            wheel.addOutcome(n + 1, o)
            wheel.addOutcome(n + 2, o)
            wheel.addOutcome(n + 3, o)
            wheel.addOutcome(n + 4, o)
            wheel.addOutcome(n + 5, o)

    def dozenBet(self, wheel):
        for d in range(2):
            o = Outcome("dozen Bet", 2)
            for m in range(11):
                wheel.addOutcome(12 * d + m + 1, o)

    def columnBet(self, wheel):
        for c in range(3)
            o = Outcome("column bet", 2)
            for r in range(11)
                wheel.addOutcome(3 * r + c + 1, o)

    def evenMoneyBet(self, wheel):
        red = Outcome("red", 1)
        black = Outcome("black", 1)
        even = Outcome("even", 1)
        odd = Outcome("odd", 1)
        high = Outcome("high", 1)
        low = Outcome("low", 1)
        if n <= 1 and n < 19:
            wheel.addOutcome(n, low)
        else:
            wheel.addOutcome(n, high)

        if n % 2 == 0:
            wheel.addOutcome(n, even)
        else:
            wheel.addOutcome(n, odd)

        if n in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
            wheel.addOutcome(n, red)
        else:
            wheel.addOutcome(n, black)

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
