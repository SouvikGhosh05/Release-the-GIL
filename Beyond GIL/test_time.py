from timeit import default_timer as timer
import add_n_sub


def with_cython(a: int, b: int):
    t = timer()

    r1 = add_n_sub.adder_py(a, b)
    r2 = add_n_sub.subtractor_py(a, b)

    print(r1)
    print(r2)
    return f"Cython took {timer()-t} seconds."


def with_python(func):
    def wrapper(a: int, b: int):
        t = timer()
        print(func(a, b))
        return timer() - t

    return wrapper


@with_python
def adder(a, b):
    for i in range(b):
        a += i
    return a


@with_python
def subtractor(a, b):
    for i in range(b):
        a -= i
    return a


if __name__ == "__main__":
    """
    Python single thread vs Cython multi thread performance
    """
    a, b = 40000000, 10000000
    print(with_cython(a, b))  # Cython took 0.0405 seconds(approx).
    print(
        f"Python took {adder(a,b)+subtractor(a,b)} seconds."
    )  # Python took 2.363 seconds(approx).
