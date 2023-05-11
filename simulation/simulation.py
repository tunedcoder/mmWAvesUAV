import numpy as np
import pandas as pd
import xarray as xr
from .objects import user, uav, blocker
from .objects.utils.los import check_pl,check_los
class Simulation():
    def __init__(self,radius ,n_users, user_height,n_uavs, uav_avg_height, uav_v_height, n_blockers, blocker_height,p_threshold= -70):
        self.r = radius
        self.area = np.pi * self.r**2

        self.user_height = user_height
        self.uav_avg_height = uav_avg_height
        self.uav_v_height = uav_v_height
        self.blocker_height = blocker_height

        self.p_threshold = p_threshold

        
        if n_users < 1:
            self.n_users = int(n_users *self.area)
        else:
            self.n_users = n_users
        
        if n_uavs < 1:
            self.n_uavs = int(n_uavs *self.area)
        else:
            self.n_uavs = n_uavs
        
        if n_blockers < 1:
            self.n_blockers = int(n_blockers *self.area)
        else:
            self.n_blockers = n_blockers
        
        self.users = []
        self.uavs = []
        self.blockers = []
        self.r_links = {}
        self.b_links = {}
        
        self._generate_users(user_height)
        self._generate_uavs(uav_avg_height, uav_v_height)
        self._generate_blockers(blocker_height)
        self._find_links()
    
        self.simulation_alive = False
    
    def _generate_users(self, user_height):
        for i in range(self.n_users):
            self.users.append(user.User(i,self.r, user_height))
    
    def _generate_uavs(self, uav_avg_height, uav_v_height):
        for i in range(self.n_uavs):
            self.uavs.append(uav.UAV(i,np.random.uniform(0,self.r,1), uav_avg_height, uav_v_height))
    
    def _generate_blockers(self, blocker_height):
        for i in range(self.n_blockers):
            self.blockers.append(blocker.Blocker(i,np.random.uniform(10,self.r,1), blocker_height))
    
    def _find_links(self):
        for u in self.users:
            self.r_links[u.id] = {}
            self.b_links[u.id] = {}
            for uav in self.uavs:
                self.r_links[u.id][uav.id] = check_pl(u.position,uav.position,self.blockers)>=self.p_threshold
                self.b_links[u.id][uav.id] = (check_los(u.position,uav.position,self.blockers))==False
                # print(self.b_links[u.id][uav.id])
    
    def _update(self):
        for u in self.users:
            u.update()
        for b in self.blockers:
            b.update()
        for uav in self.uavs:
            uav.update()

    def refresh(self):
        self.users,self.uavs,self.blockers,self.links = [],[],[],{}

        self._generate_users(self.user_height)
        self._generate_uavs(self.uav_avg_height, self.uav_v_height)
        self._generate_blockers(self.blocker_height)
        self._find_links()

    def run_simulation(self):
        self.simulation_alive = True
        while self.simulation_alive:
            self._update()

def mc_simulation(s):
    # print(l)
    r,b = [],[]
    for i in range(500):
        for u in s.users:
            # print(s.r_links[u.id],s.b_links[u.id])
            r.append(sum(s.r_links[u.id].values())/len(s.r_links[u.id]))
            b.append(sum(s.b_links[u.id].values())/len(s.b_links[u.id]))
        s.refresh()
    # print(b)
    return np.array(r).mean(),np.array(b).mean()