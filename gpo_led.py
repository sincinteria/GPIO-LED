# sincinteria
import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT) #SETUP GPIO

array =[
[0,1,1,1,0.3], #0-LED_ON,1-LED_OFF, 0.3 ms DELAY
[1,0,1,1,0.3],
[1,1,0,1,0.3],
[1,1,1,0,0.3],
[1,1,1,0,0.1],
[1,1,0,1,0.1],
[1,0,1,1,0.1],
[0,1,1,1,0.1],
[0,0,1,1,0.1],
[1,1,0,0,0.1],
[0,0,1,1,0.1],
[1,1,0,0,0.1],
[0,0,0,0,0.3],
[1,1,0,1,0.2],
[1,0,1,1,0.1],
[1,1,0,1,0.2],
[1,0,1,1,0.1],
[1,1,0,1,0.2],
[1,0,1,0,0.1],
[0,0,0,0,0.2],
[1,1,1,1,0.3]
]

try:
    while True:                     #repeat until Ctrl+c
     for i in range(len(array)):
        GPIO.output(2, array[i][0]) #2,3,4,17-number GPIO
        GPIO.output(3, array[i][1])
        GPIO.output(4, array[i][2])
        GPIO.output(17,array[i][3])
        print array[i][0],array[i][1],array[i][2],array[i][3] #comment this line after test done 
        sleep(array[i][4])

except KeyboardInterrupt:
    GPIO.cleanup()    



 
