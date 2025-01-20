import time
from Decorator import *


@timer
def check_system():
    time.sleep(2)


@timer
def check_memory():
    return "Normal!"


@morning
def say_good_morning(name):
    print(f"Good morning, {name}")


@demo(2) # how to customize the interval
def countdown(from_num):
    if from_num < 1:
        print(f"Finished")
    else:
        print(from_num)
        countdown(from_num - 1)

# customize different separators for different log levelss
@separator("*")
@separator("#")
@separator("!")
def print_info():
    print(f"INFO: The system is working well!")

@separator("#")
def print_warning():
    print(f"WARNING: The memory is low!")

@separator("!")
def print_error():
    print(f"ERROR: The system is not responding!")


print_info()
