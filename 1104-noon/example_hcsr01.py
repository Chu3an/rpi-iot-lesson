import time

from RPi import GPIO

if __name__ == "__main__":
    PIR_PIN = 18
    LED_PIN = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)
    GPIO.setup(LED_PIN, GPIO.OUT)
    try:
        while True:
            GPIO.output(LED_PIN, GPIO.input(PIR_PIN))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Bye')
    finally:
        GPIO.cleanup()