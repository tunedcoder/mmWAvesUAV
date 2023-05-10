import numpy as np
from .utils.position import get_random_position

class UAV():
    def __init__(self, i, r, avg_height, v_height):
        self.id = i
        pos = get_random_position(r)
        # print(pos)
        self.position = np.array([pos[0][0],pos[1][0] , avg_height + np.random.normal(0, v_height)])
        self.battery = 100
        self.working = True
    
    def move(self,delta):
        self.position += delta

    def update(self):
        self.battery -= config.battery_factor*height
        if self.battery <= 0:
            self.working = False