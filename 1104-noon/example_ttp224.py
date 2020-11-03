import time

from RPi import GPIO

if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    PAD_Pin = 17
    LED_Pin = 27
    GPIO.setup(PAD_Pin, GPIO.IN)
    GPIO.setup(LED_Pin, GPIO.OUT)
    light = False
    try:
        a = 0
        while True:
            if GPIO.input(PAD_Pin):
                print(a)
                a += 1
    except KeyboardInterrupt:
        print('Bye')
    finally:
        GPIO.cleanup()
