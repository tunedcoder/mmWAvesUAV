import numpy as np

def get_random_angle():
    return np.random.uniform(0, 2*np.pi)

def get_random_position(r):
    angle = get_random_angle()
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    return np.array([x,y])