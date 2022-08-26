import board
import displayio
import adafruit_ssd1327
import time

displayio.release_displays()

# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)

WIDTH = 128
HEIGHT = 128
BORDER = 1
FONTSCALE = 1

display = adafruit_ssd1327.SSD1327(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

# Draw a background rectangle, but not the full display size
color_bitmap = displayio.Bitmap(
    display.width, display.height, 1
)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White
bg_sprite = displayio.TileGrid(
    color_bitmap, pixel_shader=color_palette, x=0, y=0
)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER*2, display.height - BORDER*2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x444444  # Gray
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

while True:
    time.sleep(10)
    pass
