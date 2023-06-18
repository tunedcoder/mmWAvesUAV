import numpy as np

class User():
    def __init__(self, i, r, height):
        self.id = i
        self.position = np.array([0,0,height])
    