import matplotlib.pyplot as plt
import config as cfg

def plot_simulation(s):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(-s.radius, s.radius)
    ax.set_ylim(-s.radius, s.radius)
    ax.set_zlim(0, 10)
    ax.set_title("Simulation")
    for u in s.users:
        u.draw(ax)
    for b in s.blockers:
        b.draw(ax)
    for d in s.uavs:
        d.draw(ax)
    plt.show()

