from inspect import Traceback
from msilib.schema import File


def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
if __name__ == '__main__':
    main()
    def main():
        try:
            configuration = open('config.txt')
        except FileNotFoundError:
            print("Couldn't find the config.txt file!")
        except IsADirectoryError:
            print("Found config.txt but it is a directory, couldn't read it")
        except (BlockingIOError, TimeoutError):
            print("Filesystem under heavy load, can't complete reading configuration file")




def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"

water_left(5, 100, 2)
'Total water left after 2 days is: -10 liters'


def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"



try:
    water_left(5, 100, 2)
except RuntimeError as err:
    alert_navigation_system(err)

