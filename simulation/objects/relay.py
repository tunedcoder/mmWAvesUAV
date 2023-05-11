import numpy as np
from uav import UAV

class Relay(UAV):
    def __init__(self, i, r, avg_height, v_height):
        super().__init__(i, r, avg_height, v_height)
        self.battery = 100
        self.working = True
        self.connected = []
        self.links = {}

    def change_position(self, new_position):
        self.position = new_postion
    
    
