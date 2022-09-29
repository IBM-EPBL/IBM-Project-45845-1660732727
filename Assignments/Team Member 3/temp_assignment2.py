import random
import time

actual_time = time.time()
while True:
    temp = random.uniform(15, 25)
    time.sleep(3)
    if (temp >21):
        print("Alarm turn ON")
    else:
        print("Alarm turn OFF")
    if actual_time + 40 <time.time():
        print("Entire system turn DOWN")
        break
