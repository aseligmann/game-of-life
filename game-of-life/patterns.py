#!/usr/bin/python3

from grid import Grid


class Pattern:
    def __init__(self):
        pass

    def populate(self, grid, x, y):
        pass


class Pulsar(Pattern):
    def populate(self, grid: Grid, x, y):
        # Inner lines
        # Vertical
        for i in range(x - 4, x - 1):
            grid.populate(i, x - 1)
        for i in range(x - 4, x - 1):
            grid.populate(i, x + 1)
        for i in range(x + 2, x + 5):
            grid.populate(i, x - 1)
        for i in range(x + 2, x + 5):
            grid.populate(i, x + 1)
        # Horizontal
        for j in range(y - 4, y - 1):
            grid.populate(y - 1, j)
        for j in range(y - 4, y - 1):
            grid.populate(y + 1, j)
        for j in range(y + 2, y + 5):
            grid.populate(y - 1, j)
        for j in range(y + 2, y + 5):
            grid.populate(y + 1, j)

        # Outer lines
        # Vertical
        for i in range(x - 4, x - 1):
            grid.populate(i, x - 6)
        for i in range(x - 4, x - 1):
            grid.populate(i, x + 6)
        for i in range(x + 2, x + 5):
            grid.populate(i, x - 6)
        for i in range(x + 2, x + 5):
            grid.populate(i, x + 6)
        # Horizontal
        for j in range(y - 4, y - 1):
            grid.populate(y - 6, j)
        for j in range(y - 4, y - 1):
            grid.populate(y + 6, j)
        for j in range(y + 2, y + 5):
            grid.populate(y - 6, j)
        for j in range(y + 2, y + 5):
            grid.populate(y + 6, j)
