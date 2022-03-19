import threading
from queue import Queue
from timeit import default_timer as timer
import urllib.request
import sys


q = Queue()  # Queue technique to pass returns among threads while running


def decrement(numbers, from_start=None):  # CPU bound
    while numbers > 0:
        numbers -= 1
        if q.empty():
            continue
        """
            I added this method because this thread will run most of the time because it's mostly CPU bound

            """
        print(numbers)
        print(q.get(block=False), end="\n")
        print(
            "Time took get response after starting threads:-", timer() - from_start
        )  # It tell when exactly I/O bound returns value after both the threads started to run


def get_data():  # I/O bound

    with urllib.request.urlopen("https://www.google.com") as dt:
        q.put(dt.read(), block=False)


def call_with_threads(digit):
    """
    sys.setswitchinterval() is needed to set the time of interval for swiching among threads to reacquire GIL

    """
    sys.setswitchinterval(0.0000000000001)

    t1 = threading.Thread(target=get_data)
    t2 = threading.Thread(target=decrement, args=(digit, start))
    t1.start()
    t2.start()

    t1.join()
    t2.join()


def call_without_threads(digit):
    decrement(digit)
    get_data()


if __name__ == "__main__":
    start = timer()
    call_with_threads(1000000)
    print("Using threads took:-", timer() - start)

    start = timer()
    call_without_threads(1000000)
    print("Not using threads took:-", timer() - start)
