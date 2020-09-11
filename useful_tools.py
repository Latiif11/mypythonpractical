import  random

feet_in_mile = 5280
meters_in_kilometer = 1000
beats = ["John Lennon", "Pual McCartney", "George Harrison", "Ribgo Star"]


def get_file_ext(filname):
    return filname[filname.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)
