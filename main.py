from simulation.simulation import Simulation
from simulation.objects.utils.plotting import plot_simulation
import config
def main():
    
    s = Simulation(radius=config.R , n_users=1, user_height=1.4 , n_uavs=0.0005, uav_avg_height=5, uav_v_height=0.5, n_blockers=0.001, blocker_height=1.8)
    plot_simulation(s)
if __name__ == "__main__":
    main()