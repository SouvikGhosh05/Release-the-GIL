from timeit import default_timer as timer
from multiprocessing import Process
from numba import jit


@jit(nopython=True, fastmath=True)
def decrement(num):
    while num > 0:
        num -= 1


if __name__ == "__main__":
    start = timer()
    processes = []
    for i in [100000000, 200000000]:
        p = Process(target=decrement, args=(i,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print(timer() - start)  # 1.7067 seconds(approx)

    start = timer()
    decrement(100000000)
    decrement(200000000)
    print(timer() - start)  # 0.3143 seconds(approx)

    """
    Using processes with numba, it took more time than not using processes.
    That's because numba is a JIT compiler runs on LLVM, which is a compiler that compiles Python code to machine code.
    That means numba is already fast enough to execute sequential tasks.
    Using processes, it took more time because of spawing and destroying processes.
    Numba is not designed to run in separate processes. That's it's not recommended to run numba in separate processes.
    """
