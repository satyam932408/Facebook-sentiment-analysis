import random

five_syllables = [
    "Soft winds gently pass",
    "Stars echo the night sky",
    "Raindrops hum lightly",
    "Old trees whisper tales",
    "Morning paints the hills"
]

seven_syllables = [
    "Shadowed paths curl through the forest",
    "Silent rivers carry old secrets",
    "Golden light warms the sleeping earth",
    "Wandering thoughts drift with the breeze",
    "Frosted windows frame quiet dreams"
]

def random_haiku():
    line1 = random.choice(five_syllables)
    line2 = random.choice(seven_syllables)
    line3 = random.choice(five_syllables)
    return f"{line1}\n{line2}\n{line3}"

print(random_haiku())
