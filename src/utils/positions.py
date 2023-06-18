import numpy as np

def PolartoCartesian(P, dim=2):
    if dim == 2:
        x = P[0] * np.cos(P[1])
        y = P[0] * np.sin(P[1])
        return np.array((x, y))
    if dim == 3:
        x = P[0] * np.cos(P[1]) * np.sin(P[2])
        y = P[0] * np.sin(P[1]) * np.sin(P[2])
        z = P[0] * np.cos(P[2])
        return np.array((x, y, z))

def CartesiantoPolar(P, dim=2):
    if dim == 2:
        r = np.sqrt(P[0]**2 + P[1]**2)
        theta = np.arctan2(P[1], P[0])
        return np.array((r, theta))
    if dim == 3:
        r = np.sqrt(P[0]**2 + P[1]**2 + P[2]**2)
        theta = np.arctan2(P[1], P[0])
        phi = np.arctan2(np.sqrt(P[0]**2 + P[1]**2), P[2])
        return np.array((r, theta, phi))

def generate_random_position(dim=2,distribution="g"):
    if distribution == "g":
        return np.array(np.random.normal(0, 1, dim))
    elif distribution == "p":
        pass
    elif distribution == "u":
        return np.append(np.random.uniform(0, 1, 1),np.random.uniform(-1, 1, dim-1))
    else:
        raise ValueError("Invalid distribution type")