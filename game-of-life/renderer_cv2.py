#!/usr/bin/python3

import cv2 as cv
import numpy as np


class Renderer:
    def __init__(self, size):
        self.size = size
        self.init_window()
        self.init_scene()

    def init_window(self):
        self.window_name = "Game of Life"
        cv.namedWindow(self.window_name, cv.WINDOW_NORMAL)

    def init_scene(self):
        self.size_x = self.size
        self.size_y = self.size
        self.size_z = 1

        self.img = np.zeros((self.size_y, self.size_x, 3), np.uint8)

    def render(self, state):
        state_array = np.array(state, dtype=np.uint8)
        img_state = state_array.squeeze() * 255
        self.img = cv.cvtColor(img_state, cv.COLOR_GRAY2BGR)

        resized = cv.resize(self.img, (1000, 1000), interpolation=cv.INTER_NEAREST)
        cv.imshow(self.window_name, resized)
        cv.resizeWindow(self.window_name, resized.shape[0], resized.shape[1])
        cv.waitKey(1)


if __name__ == "__main__":
    size = 25
    renderer = Renderer(size)

    import random

    for i in range(100):
        state_rand = [
            [[random.choice([True, False]) for i in range(size)] for j in range(size)]
            for k in range(1)
        ]
        renderer.render(state_rand)
        cv.waitKey(100)
