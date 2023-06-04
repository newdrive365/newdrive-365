import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        clear()
        print("Remaining Time: ", end="")
        print("{:02d}:{:02d}".format(*divmod(seconds, 60)))
        time.sleep(1)
        seconds -= 1

    clear()
    print("Time's up! Take a break.")

if __name__ == "__main__":
    focus_timer(25)
