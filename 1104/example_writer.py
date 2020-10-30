import time

from mfrc522 import SimpleMFRC522
from RPi import GPIO

if __name__ == "__main__":
    writer = SimpleMFRC522()
    card_text = input('Input: ')
    print("Please hold a tag near the reader.")
    writer.write(card_text)
    print("Write success.")
    GPIO.cleanup()
