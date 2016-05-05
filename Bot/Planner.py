# -*- coding: utf-8 -*-
# Python3.4*

from Bot.Strategies.RandomStrategy import RandomStrategy
from Bot.Strategies.FirstStrat import FirstStrat

def create(strategyType, game, w1=1.0, w2=0.0):
    switcher = {
        "random": RandomStrategy(game),
        "strat1": FirstStrat(game, w1, w2)
    }

    strategy = switcher.get(strategyType.lower())

    return Planner(strategy)


class Planner:
    def __init__(self, strategy):
        self._strategy = strategy

    def makeMove(self):
        return self._strategy.choose()
