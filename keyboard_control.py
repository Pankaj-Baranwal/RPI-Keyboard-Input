from gpiozero import Motor
import time
#from gpiozero.Pin import
#import RPi.GPIO as GPIO

mr = Motor(3, 2)
ml = Motor(15, 14)
ml.stop()
mr.stop()



try:
    def forward():
        ml.forward(0.6)
        mr.forward(0.6)

    def backward():
        ml.backward(0.7)
        mr.backward(0.7)

    
        
    def sstop():
        ml.stop()
        mr.stop()
except KeyboardInterrupt:
    print "cleaning"
finally:
    #GPIO.cleanup()
    print"check it"


while(True):
    print "Entering"
    if (raw_input()=='w'):
        print "forward"
        forward()
    elif raw_input()=='s':
        print "backward"
        backward()
    elif raw_input()=='a':
        print "left"
        ml.backward(0.5)
        mr.forward(0.5)
    elif raw_input()=='d':
        print "right"
        mr.backward(0.5)
        ml.forward(0.5) 
    else:
        sstop()
        print "stopped"