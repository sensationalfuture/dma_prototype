import board
import neopixel
import asyncio

# Configuration
PIXEL_PIN = board.EXTERNAL_NEOPIXELS # Choose your microcontroller or Raspberry Pi GPIO pin (e.g., board.D18 or board.D0)
NUM_PIXELS = 8            # Total number of LEDs in your strip or ring
BRIGHTNESS = 0.2           # Set brightness level from 0.0 (off) to 1.0 (full)

# RGBW Order: Typically RGBW or GRBW depending on your specific LED strip manufacturer (e.g., SK6812 is often GRBW)
PIXEL_ORDER = neopixel.RGBW

# Initialize the NeoPixel object
pixels = neopixel.NeoPixel(
    PIXEL_PIN,
    NUM_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False,      # Set to False so pixels update only when pixels.show() is called
    pixel_order=PIXEL_ORDER
)

# Define 4-element tuples: (Red, Green, Blue, White)
        #(G,R,B,W)
GREEN = (255, 0, 0, 0)
RED = (0, 255, 0, 0)
BLUE = (0, 0, 255, 0)
WHITE = (0, 0, 0, 175)      # Pure white channel
WARM_MIX = (100, 50, 0, 150) # Combination of RGB + White

async def buffer():
    pixels.show()
    await asyncio.sleep(.5)


async def neostrip():
    try:
        while True:
            # Turn all pixels pure white using the dedicated W channel
            pixels.fill(WHITE)
            pixels.show()
            await asyncio.sleep(1)

            # Turn all pixels red
            pixels.fill(RED)
            pixels.show()
            await asyncio.sleep(1)

            # Set an individual pixel (pixel 0) to a warm mix
            for i in range(NUM_PIXELS):
                pixels[i] = GREEN
                await buffer()
                
    except KeyboardInterrupt:
        # Turn off all pixels cleanly on exit
        pixels.fill((0, 0, 0, 0))
        pixels.show()

print("working")

if __name__ == "__main__":
    main()