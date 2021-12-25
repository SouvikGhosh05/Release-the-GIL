from threading import Thread
from timeit import default_timer as timer
import requests


def get_data():
    requests.get("https://www.google.com")  # This is I/O bound call, which releases GIL


def using_thread():
    """
    As this thread runs on I/O bound task, using thread will improve the overall performance because of concurrency.

    """
    start = timer()
    threads = []
    for _ in range(100):
        t = Thread(target=get_data)  # Calling function using Thread
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return timer() - start


def without_thread():
    """
    This is not implemented using thread, so it will run squentially(one after another).

    """
    start = timer()
    for _ in range(100):
        get_data()  # Calling function without using Thread
    return timer() - start


if __name__ == "__main__":
    print(using_thread())  # Output: 1.20 seconds(average)
    print(without_thread())  # Output: 33.848 seconds(average)
