import concurrent.futures as fut
from timeit import default_timer as timer


def decrement(numbers):
    while numbers > 0:
        numbers -= 1


def main():
    t = timer()
    with fut.ThreadPoolExecutor() as executor:
        numbers = [10000000, 20000000]
        results = executor.map(decrement, numbers)

    return timer() - t


if __name__ == "__main__":
    print(main())  # 2.2085 seconds(approx)

    time = timer()
    decrement(10000000)
    decrement(20000000)
    print(
        "Time taken:", timer() - time, "seconds"
    )  # Time taken: 1.3332 seconds(approx)

    """
    The tasks are CPU bound operation, which needs GIL for execution.
    In Python, GIL is a global lock that prevents multiple threads from executing at the same time.
    Using threads, it look longer time because of extra time that needed for switching between threads. 
    """
