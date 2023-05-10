import numpy as np
from objects import user, uav, blocker
  
class Simulation():
    def __init__(self,radius ,n_users, user_height,n_uavs, uav_avg_height, uav_v_height, n_blockers, blocker_height ):
        self.r = radius
        self.area = np.pi * self.r**2
        
        if n_users < 1:
            self.n_users = n_users *self.area
        else:
            self.n_users = n_users
        
        if n_uavs < 1:
            self.n_uavs = n_uavs *self.area
        else:
            self.n_uavs = n_uavs
        
        if n_blockers < 1:
            self.n_blockers = n_blockers *self.area
        else:
            self.n_blockers = n_blockers
        
        self.generate_users(user_height)
        self.generate_uavs(uav_avg_height, uav_v_height)
        self.generate_blockers(blocker_height)
    
    def generate_users(self, user_height):
        self.users = []
        for i in range(self.n_users):
            self.users.append(User(self.r, user_height))
    
    def generate_uavs(self, uav_avg_height, uav_v_height):
        self.uavs = []
        for i in range(self.n_uavs):
            self.uavs.append(Uav(self.r, uav_avg_height, uav_v_height))
    
    def generate_blockers(self, blocker_height):
        self.blockers = []
        for i in range(self.n_blockers):
            self.blockers.append(Blocker(self.r, blocker_height))
    