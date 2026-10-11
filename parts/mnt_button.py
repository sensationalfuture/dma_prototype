import asyncio
import board
import digitalio
from parts.speaker import beep

async def button():
    moment_button = digitalio.DigitalInOut(board.A0)
    moment_button.switch_to_input(pull=digitalio.Pull.UP)

    while True:
        if not moment_button.value:  
            await beep(0.1)
            await asyncio.sleep(0.3)  
        await asyncio.sleep(0.01)     