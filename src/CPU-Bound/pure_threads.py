from threading import Thread
from timeit import default_timer as timer


def decrement(numbers):
    while numbers > 0:
        numbers -= 1


if __name__ == "__main__":
    time = timer()
    threads = []
    for i in [10000000, 20000000]:
        t = Thread(target=decrement, args=(i,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(
        "Time taken:", timer() - time
    )  # Time taken: 2.205 seconds(approx), same as using concurrent.futures.ThreadPoolExecutor()

    """
    So, using concurrent.futures.ThreadPoolExecutor() and using threads, is the same benefit for performance.
    """
