# -*- coding: utf-8 -*-
# Python3.4*

from sys import stdin, stdout
import sys
from Bot import Planner
from Bot.Game.Game import Game
from Bot.Parser import Parser


class Bot:
    def __init__(self, strategy, w1=1.0, w2=0.0, p=True):
        self.game = Game()
        self._parser = Parser(self.game)
        self._planner = Planner.create(strategy, self.game, w1, w2)
        self.fname = 'p3_output.txt'
        self.p = p
        if p:
            self.my_output = open(self.fname,'w')

    def run(self):
        while not stdin.closed:
            try:
                line = stdin.readline().strip()

                if len(line) == 0:
                    continue
                if line == 'bob':
                    exit()
                if self.p:
                    self.my_output.write(line+'\n')
                moves = self.interpret(line)

                if moves:
                    self.sendMoves(moves)

            except EOFError:
                if self.p:
                    self.my_output.close()
                self.strategy.close()
                return

    def interpret(self, line):
        if line.startswith('action'):
            return self._planner.makeMove()
        else:
            self._parser.parse(line)

    @staticmethod
    def sendMoves(moves):
        stdout.write(','.join(moves) + '\n')
        stdout.flush()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        Bot("strat1", w1=float(sys.argv[1]), w2=float(sys.argv[2])).run()
    Bot('strat1').run()