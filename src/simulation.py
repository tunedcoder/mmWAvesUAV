import numpy as np

from objects.user import User
from objects.uav import UAV
from objects.blocker import Blocker
from utils.positions import generate_random_position, PolartoCartesian
import config as cfg


class Simulation:
    def __init__(self) -> None:
        print("Works")
        self.users = []
        self.uavs = []
        self.blockers = []
        self.links = []

        self.radius = cfg.R

        self._generate_users()
        self._generate_uavs()
        self._generate_blockers()

        # self._generate_links()

        # self.check_links()

        print(self.blockers)

    def _generate_users(self):
        for i in range(cfg.N_USERS):
            if i == 0:
                self.users.append(User(i + 1, np.array((0, 0, cfg.USER_HEIGHT))))
            else:
                self.users.append(
                    User(
                        i + 1,
                        np.array(
                            np.append(
                                PolartoCartesian(
                                    generate_random_position(distribution="u")
                                    * np.array([cfg.R, 360])
                                ),
                                cfg.USER_HEIGHT,
                            )
                        ),
                    )
                )

    def _generate_uavs(self):
        if cfg.UAV_DENSITY < 1:
            self.N_UAVS = int(cfg.UAV_DENSITY * cfg.AREA)
        else:
            self.N_UAVS = cfg.UAV_DENSITY
        for i in range(self.N_UAVS):
            self.uavs.append(
                UAV(
                    i + 1,
                    np.array(
                        np.append(
                            PolartoCartesian(
                                generate_random_position(distribution="u")
                                * np.array([cfg.R, 360])
                            ),
                            cfg.UAV_MEAN_HEIGHT,
                        )
                    ),
                )
            )

    def _generate_blockers(self):
        if cfg.BLOCKER_DENSITY < 1:
            self.N_BLOCKERS = int(cfg.BLOCKER_DENSITY * cfg.AREA)
        else:
            self.N_BLOCKERS = cfg.BLOCKER_DENSITY
        for i in range(self.N_BLOCKERS):
            self.blockers.append(
                Blocker(
                    i + 1,
                    np.array(
                        np.append(
                            PolartoCartesian(
                                generate_random_position(distribution="u")
                                * np.array([cfg.R, 360])
                            ),
                            cfg.BLOCKER_HEIGHT,
                        ),
                    ),
                    cfg.BLOCKER_WIDTH_R,
                )
            )
