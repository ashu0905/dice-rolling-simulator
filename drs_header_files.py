import random
choice = chr
roll = int
dice = int
min = int
max = int
dice_choice = chr
spectrum = int
result = ""
dice = [1, 2, 3, 4, 5, 6]
min = 1
max = 50
spectrum = range(min, max)
def dice_func():
    roll = random.choice(dice)
    result = "You rolled a {}".format(roll)
    return result
def spectrum_func():
    roll = random.choice(spectrum)
    result = "You rolled a {}".format(roll)
    return result
