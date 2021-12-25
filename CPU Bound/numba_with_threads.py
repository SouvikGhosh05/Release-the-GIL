from threading import Thread
from timeit import default_timer as timer
from numba import jit


@jit(nopython=True, fastmath=True, nogil=True)
def decrement(num):
    while num > 0:
        num -= 1


def with_thread() -> str:
    time = timer()
    threads = []
    for i in [100000000, 200000000]:
        t = Thread(target=decrement, args=(i,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return f"Time taken: {timer()-time} seconds"


def without_thread():
    start = timer()
    decrement(10000000000)
    decrement(20000000000)

    return timer() - start


if __name__ == "__main__":

    print(with_thread())  # Time taken: 0.3242 seconds
    print(without_thread())  # Time taken: 1.0599e-05 seconds

    """
    Without threads, it took less time to execute using numba.
    So, numba is still not properly releasing GIL for parallel execution of tasks.
    So, numba is also not recommended to release GIL to get parallelism.
    Then, It's now time to use Cython to our get work done.
    """
