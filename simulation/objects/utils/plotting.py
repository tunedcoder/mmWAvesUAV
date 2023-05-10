import matplotlib.pyplot as plt
import numpy as np

def plot_simulation(s):
    
    plot = plt.figure()
    ax = plot.add_subplot(111, projection='3d')
    ax.set_xlim(-s.r,s.r)
    ax.set_ylim(-s.r,s.r)
    ax.set_zlim(0,30)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    users = s.users
    for u in users:
        ax.scatter(u.position[0],u.position[1],u.position[2],c='k',marker='o')
        # draw a line from (0,0,0) to user height
        ax.plot([0,0],[0,0],[0,u.position[2]],c='k')
        user_links = s.links[u.id]
        print(user_links)
        # break
        for d in user_links:
            if user_links[d] == "relaible":
                ax.scatter(s.uavs[d].position[0],s.uavs[d].position[1],s.uavs[d].position[2],c='g',marker='o')
                ax.plot([u.position[0],s.uavs[d].position[0]],[u.position[1],s.uavs[d].position[1]],[u.position[2],s.uavs[d].position[2]],c='g',linestyle='--')
            else:
                ax.scatter(s.uavs[d].position[0],s.uavs[d].position[1],s.uavs[d].position[2],c='r',marker='o')
                ax.plot([u.position[0],s.uavs[d].position[0]],[u.position[1],s.uavs[d].position[1]],[u.position[2],s.uavs[d].position[2]],c='r',linestyle='--')
    
    for b in s.blockers:
        ax.scatter(b.position[0],b.position[1],b.position[2],c='b',marker='o')
        ax.plot([b.position[0],b.position[0]],[b.position[1],b.position[1]],[0,b.position[2]],c='b',linestyle='--')

    plt.show()