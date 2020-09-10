import time

def counter(name, number):
    for i in range(number):
        print('%6s: %d' % (name, i))
        time.sleep(1)

if __name__ == "__main__":
    counter('Alpha', 5)
    counter('Beta', 3)
