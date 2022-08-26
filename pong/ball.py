from .colors import Colors
from .game_element import GameElement
from .game_config import GameConfig
from .coords import Coords
from displayio import Bitmap, Group, Palette, TileGrid
import math
import random

class Ball(GameElement):

    def __init__(self) -> None:
        self.ball_group: Group = Group()
        self.coords: Coords = Coords()

    def setup(self) -> None:
        self.palette: Palette = Palette(color_count=1)
        self.palette[0] = Colors.WHITE
        self.bitmap: Bitmap = Bitmap(GameConfig.BALL_WIDTH, GameConfig.BALL_HEIGHT, 1)
        self.bitmap.fill(0)
        self.tileGrid: TileGrid = TileGrid(bitmap=self.bitmap, pixel_shader=self.palette, x=0, y=0)
        self.ball_group.append(self.tileGrid)

    def reset(self) -> None:
        self.coords.x = GameConfig.PLAYGROUND_WIDTH / 2
        self.coords.y = GameConfig.PLAYGROUND_HEIGHT / 2 + GameConfig.PLAYGROUND_TOP
        self.ball_radial = (random.random() * math.pi / 2 - math.pi / 4) % (2 * math.pi)
        self.ball_velocity = GameConfig.BALL_INITIAL_VELOCITY
    
    def bounceH(self, radial: float) -> float:
        return (2 * math.pi - radial) % (2 * math.pi)

    def bounceV(self, radial: float) -> float:
        return (math.pi - radial) % (2 * math.pi)

    def increaseVelocity(self) -> float:
        if self.ball_velocity < GameConfig.BALL_MAX_VELOCITY:
            self.ball_velocity *= GameConfig.BALL_ACCELERATION
        return self.ball_velocity

    def update(self) -> None:
        self.coords.x = self.coords.x + math.cos(self.ball_radial) * self.ball_velocity
        self.coords.y = self.coords.y + math.sin(self.ball_radial) * self.ball_velocity

    def draw(self) -> None:       
        self.ball_group.x = int(self.coords.x)
        self.ball_group.y = int(self.coords.y)
