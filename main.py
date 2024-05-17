import time
import random

def hello_world():
    print("Hello, World!")
    sleep_time = random.randint(1, 5)
    time.sleep(sleep_time)
    print(f"Slept for {sleep_time} seconds")

# Call the function
hello_world()

