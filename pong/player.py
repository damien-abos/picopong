from .colors import Colors
from .game_element import GameElement
from .game_config import GameConfig
from .coords import Coords
from displayio import Bitmap, Group, Palette, TileGrid
import terminalio
from adafruit_display_text import label
import math

class Player(GameElement):
    LEFT: int = 0
    RIGHT: int = 1
    INCREASE: int = 0
    DECREASE: int = 1

    def __init__(self, side: int=LEFT) -> None:
        self.side = side
        self.score = 0
        self.coords = Coords()
        self.player_group = Group()
        self.score_group = Group()

    def setup(self) -> None:
        self.palette = Palette(color_count=1)
        self.palette[0] = Colors.GREY_LIGHT
        self.bitmap = Bitmap(GameConfig.PLAYER_WIDTH, GameConfig.PLAYER_HEIGHT, 1)
        self.bitmap.fill(0)
        self.tileGrid = TileGrid(bitmap=self.bitmap, pixel_shader=self.palette, x=0, y=0)
        self.player_group.append(self.tileGrid)
        self.label = label.Label(terminalio.FONT, text=str(self.score), color=Colors.GREY)
        self.label.y = 5
        if self.side == Player.LEFT:
            self.label.x = 25
        else:
            self.label.x = GameConfig.SCREEN_WIDTH - 30
        self.score_group.append(self.label)


    def reset(self) -> None:
        self.score = 0
        self.label.text = str(self.score)
        self.velocity = GameConfig.PLAYER_INITIAL_VELOCITY
        self.direction = Player.INCREASE
        self.coords.y = (GameConfig.PLAYGROUND_HEIGHT - GameConfig.PLAYER_HEIGHT) / 2 + GameConfig.PLAYGROUND_TOP
        if self.side == Player.LEFT:
            self.coords.x = GameConfig.PLAYER_WIDTH
        else:
            self.coords.x = GameConfig.PLAYGROUND_WIDTH - GameConfig.PLAYER_WIDTH

    def moveTo(self, coords: Coords) -> float:
        if math.fabs(coords.x - self.coords.x) < 4/5 * GameConfig.PLAYGROUND_WIDTH:
            if self.coords.y < coords.y and self.coords.y < GameConfig.PLAYGROUND_TOP + GameConfig.PLAYGROUND_HEIGHT - GameConfig.PLAYER_HEIGHT:
                self.updateVelocity(Player.INCREASE)
                self.coords.y = self.coords.y + self.velocity
            elif self.coords.y > coords.y - GameConfig.PLAYER_HEIGHT:
                self.updateVelocity(Player.DECREASE)
                self.coords.y = self.coords.y - self.velocity
        return self.coords.y

    def updateVelocity(self, direction: int) -> float:
        if self.direction == direction:
            if self.velocity < GameConfig.PLAYER_MAX_VELOCITY:
                self.velocity *= GameConfig.PLAYER_ACCELERATION
        else:
            self.direction = direction
            self.velocity = GameConfig.PLAYER_INITIAL_VELOCITY
        return self.velocity

    def incrementScore(self) -> int:
        self.score += 1
        self.label.text = str(self.score)
        return self.score

    def update(self) -> None:
        pass

    def draw(self) -> None:
         self.player_group.x = int(self.coords.x)
         self.player_group.y = int(self.coords.y)