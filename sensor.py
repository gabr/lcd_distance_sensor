import RPi.GPIO as GPIO
import lcd as LCD
import time


GPIO.setmode(GPIO.BOARD)

TRIG = 12
ECHO = 16

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.1)

print "Starting Measurement..."

try:
    while True:
        time.sleep(1);

        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)

        while GPIO.input(ECHO) == 0:
            pass

        start = time.time()

        while GPIO.input(ECHO) == 1:
            pass

        stop = time.time()

        result = (stop - start) * 17000
        text = " {:.2f} cm".format(result)

        LCD.lcd_init()
        LCD.lcd_string(text)

        print text

except KeyboardInterrupt:
    GPIO.cleanup()
