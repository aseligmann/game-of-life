#!/usr/bin/python3

from time import sleep
from game import Game
from grid import Grid
from patterns import Pulsar

# from renderer_o3d import Renderer
from renderer_cv2 import Renderer


if __name__ == "__main__":
    size = 200

    grid = Grid()
    grid.empty(size)
    for i in range(10, size, 20):
        for j in range(10, size, 20):
            grid.populate(i, j)
            Pulsar().populate(grid, i, j)

    renderer = Renderer(size)
    game = Game(grid=grid)

    def update():
        renderer.render(game.getState3D())
        game.tick()

    for i in range(100):
        update()
        sleep(0.1)
