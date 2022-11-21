from .sample import roll_dice

def guess_number(num):
    result = roll_dice()
    if result == num:
        return "you win"
    else:
        return "you lost"