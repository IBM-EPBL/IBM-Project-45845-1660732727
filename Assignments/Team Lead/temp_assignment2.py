import random
import time
t1 = int(input("Enter the threshold value for temperature: "))
t2 = int(input("Enter the threshold value for humidity: "))

h = 0
t = 0

while(True):
    temp = random.uniform(1, 100)
    humidity = random.uniform(1,50)
    print("Temperature is : {0:.2f}".format(temp))
    print("Humidity is : {0:.2f} %".format(humidity))
    time.sleep(1)
    
    if temp >= t1 and humidity<= t2:
        h =1
        t = 1
        print("HIGH TEMPERATURE\nHumidity alarm and Temperature turn ON")
        time.sleep(2)
        
    elif humidity <= t2:
        h = 1
        t = 0
        print("Humidity alarm is ON and Temperature alarm is OFF")
        time.sleep(2)

    elif temp >= t1:
        h=0
        t = 1
        print("Humidity alarm is OFF and Temperature alarm is ON")
        time.sleep(2)

    else:
        h = 0
        t = 0
        print("Both alarms are OFF")
        time.sleep(2)
