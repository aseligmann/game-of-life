#!/usr/bin/python3

from time import sleep
from game import Game
from grid import Grid
from patterns import Pulsar

# from renderer_o3d import Renderer
from renderer_cv2 import Renderer


if __name__ == "__main__":
    size = 19

    grid = Grid()
    grid.empty(size)
    Pulsar().populate(grid, int(size / 2), int(size / 2))

    renderer = Renderer(size)
    game = Game(grid=grid)

    def update():
        game.tick()
        renderer.render(game.getState3D())

    for i in range(100):
        update()
        sleep(0.1)
