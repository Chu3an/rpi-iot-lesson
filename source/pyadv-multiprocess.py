import time
from multiprocessing import Process


def counter(name, number):
    for i in range(number):
        print('%6s: %d' % (name, i))
        time.sleep(1)

if __name__ == "__main__":
    ap = Process(target=counter, args=('Alpha', 5, ))
    bp = Process(target=counter, args=('Beta', 3, ))
    ap.start()
    bp.start()
    ap.join()
    bp.join()
    print('Main process down.')