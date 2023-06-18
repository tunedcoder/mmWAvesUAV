import numpy as np

R = 100
AREA = np.pi * R**2 

N_USERS=1
USER_HEIGHT = 1.4
SELF_BLOCKAGE = 0

UAV_DENSITY = 0.0001
UAV_MEAN_HEIGHT = 5
UAV_HEIGHT_STD = 1

BLOCKER_DENSITY= 0.0005
BLOCKER_HEIGHT = 1.8
BLOCKER_VELOCITY = 0
BLOCKER_WIDTH_R = 0

ALPHA_LOS = 61.4
BETA_LOS = 2

ALPHA_NLOS = 72
BETA_NLOS = 2.92


USER_COLOR = "black"
UAV_COLOR = ["green", "yellow", "red"]
BLOCKER_COLOR = "blue"