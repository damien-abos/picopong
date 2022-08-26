from pong.game_config import GameConfig
from .game_element import GameElement
from .ball import Ball
from .colors import Colors
from .player import Player
from .playground import Playground
from displayio import Display, Group
import terminalio
from adafruit_display_text import label

class Game(GameElement):

    def __init__(self, display: Display) -> None:
        self.display = display
        self.playground = Playground()
        self.player1 = Player(side = Player.LEFT)
        self.player2 = Player(side = Player.RIGHT)
        self.ball = Ball()
    
    def setup(self) -> None:
        self.playground.setup()
        self.player1.setup()
        self.player2.setup()
        self.ball.setup()
        self.game_group = Group()       
        self.game_group.append(self.playground.playground_group)
        self.game_group.append(self.player1.player_group)
        self.game_group.append(self.player1.score_group)
        self.game_group.append(self.player2.player_group)
        self.game_group.append(self.player2.score_group)
        self.game_group.append(self.ball.ball_group)
        pong_label = label.Label(terminalio.FONT, text="PONG by Dams", color=Colors.GREY_DARKER)
        pong_label.x = int((GameConfig.SCREEN_WIDTH - pong_label.width) / 2)
        pong_label.y = GameConfig.PLAYGROUND_TOP + GameConfig.PLAYGROUND_HEIGHT + 7
        self.game_group.append(pong_label)
        self.display.show(self.game_group)

    def reset(self) -> None:
        self.playground.reset()
        self.player1.reset()
        self.player2.reset()
        self.ball.reset()

    def update(self) -> None:
        self.playground.update()
        self.ball.update()
        self.player1.update()
        self.player1.moveTo(self.ball.coords)
        self.player2.update()
        self.player2.moveTo(self.ball.coords)

        player_bounce = False
        if self.ball.coords.x <= GameConfig.PLAYER_WIDTH * 2 and self.ball.coords.y >= self.player1.coords.y and self.ball.coords.y <= self.player1.coords.y + GameConfig.PLAYER_HEIGHT:
            self.ball.ball_radial = self.ball.bounceV(self.ball.ball_radial)
            self.ball.increaseVelocity()
            player_bounce = True
        elif self.ball.coords.x >= (GameConfig.PLAYGROUND_WIDTH - GameConfig.PLAYER_WIDTH * 2  - GameConfig.BALL_WIDTH) and self.ball.coords.y >= self.player2.coords.y and self.ball.coords.y <= self.player2.coords.y + GameConfig.PLAYER_HEIGHT:
            self.ball.ball_radial = self.ball.bounceV(self.ball.ball_radial)
            self.ball.increaseVelocity()
            player_bounce = True
        if self.ball.coords.y <= GameConfig.PLAYGROUND_TOP:
            self.ball.ball_radial = self.ball.bounceH(self.ball.ball_radial)
        elif self.ball.coords.y >= GameConfig.SCREEN_HEIGHT - GameConfig.PLAYGROUND_TOP - GameConfig.BALL_HEIGHT:
            self.ball.ball_radial = self.ball.bounceH(self.ball.ball_radial)
        
        if not player_bounce:
            if self.ball.coords.x <= 0:
                self.player2.incrementScore()
                self.ball.reset()
            elif self.ball.coords.x >= GameConfig.PLAYGROUND_WIDTH  - GameConfig.BALL_WIDTH:
                self.player1.incrementScore()
                self.ball.reset()

    def draw(self) -> None:
        self.playground.draw()
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        self.display.refresh(target_frames_per_second=60)

