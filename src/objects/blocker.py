import config as cfg
import numpy as np
from utils.positions import PolartoCartesian, CartesiantoPolar
import mpl_toolkits.mplot3d.art3d as art3d


class Blocker:
    def __init__(self, id, position, r):
        self.id = id
        self.position = position
        self.radius = r

    def __str__(self):
        return f"Blocker {self.id} at {self.position} with radius {self.radius} \n"

    def __repr__(self):
        return f"Blocker {self.id} at {self.position} with radius {self.radius} \n"

    def draw(self, ax, v="l"):
        if self.radius == 0:
            ax.scatter(
                self.position[0],
                self.position[1],
                self.position[2],
                color=cfg.BLOCKER_COLOR,
                marker="o",
                label="Blocker",
            )
            # draw a line from x-y plane to position
            ax.plot(
                [self.position[0], self.position[0]],
                [self.position[1], self.position[1]],
                [0, self.position[2]],
                linestyle="--",
                color=cfg.BLOCKER_COLOR,
            )
        else:
            if v == "l":
                self.polar = CartesiantoPolar(self.position, 3)
                                
                u = self.position + PolartoCartesian([self.radius, self.polar[1] + np.pi/2, np.pi/2], 3)
                l = self.position + PolartoCartesian([self.radius, self.polar[1] - np.pi/2, np.pi/2], 3)
                # print("upper", u)
                # print("center", self.position)
                # print("lower", l)

                # x = np.linspace(u[0], l[0], 10)
                # y = [self.position[2]]*10
                x = np.linspace(u[0], l[0], 10)
                z = np.linspace(0, self.position[2], 2)
                xx, zz = np.meshgrid(x,z)
                y = (self.position[0]**2 + self.position[1]**2 - xx*self.position[0] )/self.position[1]

                ax.plot_surface(xx, y, zz, color=cfg.BLOCKER_COLOR)

            elif v == "c":
                x = np.linspace(
                    self.position[0] - self.radius, self.position[0] + self.radius, 10
                )
                z = np.linspace(0, self.position[2], 2)
                X, Z = np.meshgrid(x, z)

                Y = (
                    np.sqrt(self.radius**2 - (X - self.position[0]) ** 2)
                    + self.position[1]
                )

                ax.plot_surface(X, Y, Z, linewidth=0, color=cfg.BLOCKER_COLOR)
                ax.plot_surface(
                    X,
                    (2 * self.position[1] - Y),
                    Z,
                    linewidth=0,
                    color=cfg.BLOCKER_COLOR,
                )
