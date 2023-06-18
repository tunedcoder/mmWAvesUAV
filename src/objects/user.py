import config as cfg

class User:
    def __init__(self, id, position) -> None:
        self.id = id
        self.position = position

    def __str__(self) -> str:
        return f"User {self.id} at {self.position} \n"

    def __repr__(self) -> str:
        return f"User {self.id} at {self.position} \n"

    def draw(self, ax):
        ax.scatter(
            self.position[0],
            self.position[1],
            self.position[2],
            color=cfg.USER_COLOR,
            marker="o",
            label="User",
        )
        ax.plot(
            [self.position[0], self.position[0]],
            [self.position[1], self.position[1]],
            [0, self.position[2]],
            linestyle="--",
            color=cfg.USER_COLOR,
        )
        # ax.add_patch(Circle((self.position[0], self.position[1]), self.radius, color=self.color, alpha=0.5, zorder=1))
