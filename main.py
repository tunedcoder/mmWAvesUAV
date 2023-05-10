import numpy as np
from simulation.simulation import Simulation,mc_simulation
from simulation.objects.utils.plotting import plot_simulation,plot_reliability
import config
def main():
    
    v = np.linspace(5, 15, 100)
    f = []
    for m in v:
        s = Simulation(radius=config.R , n_users=1, user_height=1.4 , n_uavs=0.0001, uav_avg_height=m, uav_v_height=0.5, n_blockers=0.001, blocker_height=2)
    # plot_simulation(s)
        f.append(mc_simulation(s))
        print(m)
    plot_reliability(v,f)

if __name__ == "__main__":
    main()