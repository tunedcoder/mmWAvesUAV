import numpy as np
from .utils.position import get_random_position, get_random_angle

class Blocker():
    def __init__(self, i, r, height):
        pos = get_random_position(r)
        self.position = np.array([pos[0][0],pos[1][0],height])
        self.velocity = np.array([get_random_position(1)])

    
    def update(self):
        self.position += self.velocity