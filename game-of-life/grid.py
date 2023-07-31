#!/usr/bin/python3


class Grid:
    def __init__(self, size=0, grid=None):
        """
        Initialize a grid
        """
        if grid is not None:
            # Initialize the grid from other
            self.grid = grid
            self.size = len(grid[0])
            return
        if size > 0:
            # Initialize the grid from size
            self.empty(size)

    def getSize(self):
        """
        Get the size of the grid
        """
        return self.size

    def empty(self, size):
        """
        Create an empty grid
        """
        self.size = size

        # Create a 2D array of size by size
        self.grid = [[False for x in range(size)] for y in range(size)]

    def expand(self, n):
        """
        Expand the grid by n cells in each direction
        """
        old_size = self.size
        new_size = old_size + n * 2

        # Create a new grid of size by size
        new_grid = [[False for x in range(new_size)] for y in range(new_size)]

        # Copy the old grid into the new grid
        center_x = int(new_size / 2)
        center_y = center_x
        for i in range(old_size):
            new_grid_i = i + center_x - int(old_size / 2)
            for j in range(old_size):
                new_grid_j = j + center_y - int(old_size / 2)
                new_grid[new_grid_i][new_grid_j] = self.grid[i][j]

        # Set the new grid as the grid
        self.size = new_size
        self.grid = new_grid

    def populate(self, x, y):
        """
        Populate a cell
        """
        self.grid[x][y] = True

    def eliminate(self, x, y):
        """
        Eliminate a cell
        """
        self.grid[x][y] = False

    def isAlive(self, x, y):
        """
        Check if a cell is alive
        """
        return self.grid[x][y]

    def getNeighbors(self, x, y):
        """
        Get the neighbors of a cell
        """
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # Own cell
                if x + i < 0 or x + i >= self.size:
                    continue  # Out of bounds
                if y + j < 0 or y + j >= self.size:
                    continue  # Out of bounds

                neighbors.append(self.grid[x + i][y + j])
        return neighbors

    def get(self):
        """
        Get the grid
        """
        return self.grid

    def print(self):
        """
        Print the grid
        """
        for i in range(self.size):
            for j in range(self.size):
                print("█" if self.grid[i][j] else "░", end="")
            print()
