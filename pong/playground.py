from pong import Colors, GameConfig, GameElement
from displayio import Bitmap, Group, Palette, TileGrid

class Playground(GameElement):

    def __init__(self) -> None:
        self.playground_group = Group()
    
    def setup(self) -> None:
        self.palette = Palette(color_count=4)
        self.palette[0] = Colors.BLACK
        self.palette[1] = Colors.GREY_DARKER
        self.palette[2] = Colors.GREY_DARK
        self.bitmap = Bitmap(GameConfig.PLAYGROUND_WIDTH, GameConfig.PLAYGROUND_HEIGHT, 4)
        self.bitmap.fill(0)
        for i in range(0, GameConfig.PLAYGROUND_WIDTH, 1):
            self.bitmap[i] = 2
            self.bitmap[GameConfig.PLAYGROUND_WIDTH * (GameConfig.PLAYGROUND_HEIGHT -1) + i] = 2
        for i in range(0, GameConfig.PLAYGROUND_WIDTH, 4):
            self.bitmap[GameConfig.PLAYGROUND_WIDTH * i + int(GameConfig.PLAYGROUND_WIDTH / 2)] = 1
        self.tileGrid = TileGrid(bitmap=self.bitmap, pixel_shader=self.palette, x=0, y=0)
        self.playground_group.append(self.tileGrid)

    def reset(self) -> None:
        x_anchor = int((GameConfig.SCREEN_WIDTH - GameConfig.PLAYGROUND_WIDTH) / 2)
        y_anchor =  GameConfig.PLAYGROUND_TOP
        self.playground_group.x = x_anchor
        self.playground_group.y = y_anchor