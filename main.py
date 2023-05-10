from simulation.simulation import Simulation
import config
def main():
    
    s = Simulation(radius=config.R , n_users=1, user_height=1.4 , n_uavs=3, uav_avg_height=5, uav_v_height=0.2, n_blockers=0.001, blocker_height=1.8)

if __name__ == "__main__":
    main()