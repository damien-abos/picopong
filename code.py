import board
import displayio
import adafruit_ssd1327
import time
import pong

class Main:

    def __init__(self) -> None:
        # Release all previous displays
        displayio.release_displays()
        # Use for I2C
        i2c = board.I2C()
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
        display = adafruit_ssd1327.SSD1327(display_bus, width=pong.GameConfig.SCREEN_WIDTH, height=pong.GameConfig.SCREEN_HEIGHT, auto_refresh=False)
        # Create a pong Game
        self.game = pong.Game(display=display)
        
    def setup(self) -> None:
        self.game.setup()

    def run(self) -> None:
        self.game.reset()
        while True:
            self.game.update()
            self.game.draw()
            #time.sleep(0.016)

if __name__ == "__main__":
    main = Main()
    main.setup()
    main.run()
