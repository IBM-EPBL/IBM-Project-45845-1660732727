import random
import time

act_time = time.time()
while True:
    temp = random.uniform(15, 25)
    time.sleep(4)
    if (temp >21):
        print("Alarm turn ON")
    else:
        print("Alarm turn OFF")
    if act_time + 30 <time.time():
        print("Entire system goes DOWN")
        break
