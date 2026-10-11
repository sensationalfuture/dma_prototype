import array
import math
import asyncio
import audiobusio
import audiocore
import board

# Build one cycle of a sine wave (a pure tone)
SAMPLE_RATE = 16000
LENGTH = SAMPLE_RATE // 440          # 440 Hz = note A
wave = array.array("h", [
    int(math.sin(2 * math.pi * i / LENGTH) * (2 ** 14))
    for i in range(LENGTH)
])
tone = audiocore.RawSample(wave, sample_rate=SAMPLE_RATE)

audio = audiobusio.I2SOut(board.I2S_BIT_CLOCK, board.I2S_WORD_SELECT, board.I2S_DATA)

async def beep(duration=0.2):
    audio.play(tone, loop=True)
    await asyncio.sleep(duration)
    audio.stop()