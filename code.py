import asyncio
import board
from digitalio import DigitalInOut, Direction

from parts.servo import servo
from parts.neostrip import neostrip
from parts.mnt_button import button

external_power = DigitalInOut(board.EXTERNAL_POWER)
external_power.direction = Direction.OUTPUT
external_power.value = True  # Turns on power to external NeoPixel 5V line

async def main():
    print("testing")
    neo_task = asyncio.create_task(neostrip())
    servo_task = asyncio.create_task(servo())
    moment_button = asyncio.create_task(button())
    
    await asyncio.gather(neo_task, servo_task,moment_button)

asyncio.run(main())