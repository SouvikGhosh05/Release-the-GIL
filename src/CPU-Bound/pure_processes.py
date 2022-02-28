from threading import Thread
from multiprocessing import Process
from timeit import default_timer as timer


def decrement(numbers):
    while numbers > 0:
        numbers -= 1


if __name__ == "__main__":
    time = timer()
    processes = []
    for i in [10000000, 20000000]:
        p = Process(target=decrement, args=(i,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print(
        "Time taken:", timer() - time, "seconds"
    )  # Time taken: 1.0308 seconds(approx)

    time = timer()
    decrement(10000000)
    decrement(20000000)
    print(
        "Time taken:", timer() - time, "seconds"
    )  # Time taken: 1.4732 seconds(approx)

    """
    Using processes, it took less time because, GIL is not issue for running in separate processes, since each process has its own GIL.
    So, multiprocessing is the way get parellism for CPU bound tasks from Python interpreter.
    """
