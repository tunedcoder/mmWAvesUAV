import config as cfg
class UAV:
    def __init__(self, id, position) -> None:
        self.id = id
        self.position = position

    def __str__(self) -> str:
        return f"UAV {self.id} at {self.position} \n"

    def __repr__(self) -> str:
        return f"UAV {self.id} at {self.position} \n"

    def draw(self, ax):
        ax.scatter(
            self.position[0],
            self.position[1],
            self.position[2],
            color=cfg.UAV_COLOR[0],
            marker="o",
            label="UAV",
        )
