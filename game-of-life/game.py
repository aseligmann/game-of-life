#!/usr/bin/python3

from grid import Grid


class Game:
    def __init__(self, size=0, grid=None):
        """
        Initialize the game
        """
        if grid is not None:
            self.grid = grid
            return
        if size > 0:
            self.grid = Grid(size=size)

    def tick(self):
        """
        Tick the game forward one step
        """

        # Initialize the next grid
        size = self.grid.getSize()
        next_grid = Grid(size=size)

        # Check every cell and apply the rules of life
        for i in range(size):
            for j in range(size):
                # Get state of cell and its neighbors
                is_alive = self.grid.isAlive(i, j)
                neighbors = self.grid.getNeighbors(i, j)
                count_alive = neighbors.count(True)
                # Apply the rules of life
                if is_alive:
                    if count_alive >= 2 and count_alive <= 3:
                        # Survive
                        next_grid.populate(i, j)
                    else:
                        # Overpopulation or underpopulation
                        next_grid.eliminate(i, j)
                else:
                    if count_alive == 3:
                        # Reproduction
                        next_grid.populate(i, j)

        # Set the next grid as the grid
        self.grid = next_grid

    def getState(self):
        """
        Get the grid
        """
        return self.grid.grid

    def getState2D(self):
        """
        Get the grid
        """
        return self.getState()

    def getState3D(self):
        """
        Get the grid
        """
        return [self.getState()]  # Grid is only implemented in 2D atm 🤷‍♂️

    def print(self):
        self.grid.print()
