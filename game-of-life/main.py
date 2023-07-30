#!/usr/bin/python3

from game import Game
from grid import Grid
from patterns import Pulsar


if __name__ == "__main__":
    grid = Grid()
    grid.empty(19)
    Pulsar().populate(grid, 9, 9)
    grid.print()

    game = Game(grid=grid)
    for i in range(10):
        print("-"*80)
        game.tick()
        game.print()
