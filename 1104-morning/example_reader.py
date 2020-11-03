import time

from mfrc522 import SimpleMFRC522
from RPi import GPIO

if __name__ == "__main__":
    reader = SimpleMFRC522()
    try:
        while True:
            print("Please hold a tag near the reader.")
            card_id, card_text = reader.read()
            print("  ID: %s" % card_id)
            print("Text: %s" % card_text)
            time.sleep(1)
    except KeyboardInterrupt:
        print('Bye')
    finally:
        GPIO.cleanup()
