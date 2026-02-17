import time
import random

with open('data.txt', 'w') as f:
    f.write("0\n")

while True:
    with open('data.txt', 'a') as f:
        f.write(f"{random.randint(1, 100)}\n")
    time.sleep(1)
    