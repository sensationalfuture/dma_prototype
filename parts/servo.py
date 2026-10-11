import asyncio
import board
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.EXTERNAL_SERVO, duty_cycle=2 ** 15, frequency=50)

new_servo = servo.Servo(pwm)
async def servo():
    while True:
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            new_servo.angle = angle
            await asyncio.sleep(1)
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            new_servo.angle = angle
            await asyncio.sleep(1)