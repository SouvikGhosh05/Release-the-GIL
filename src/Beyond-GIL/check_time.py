from timeit import default_timer as timer
import add_n_sub


def adder_cython(a: int, b: int):
    return add_n_sub.adder_py(a, b)


def subtractor_cython(a: int, b: int):
    return add_n_sub.subtractor_py(a, b)


def adder_py(a, b):
    for i in range(b):
        a += i
    return a


def subtractor_py(a, b):
    for i in range(b):
        a -= i
    return a


def with_cython(a: int, b: int):
    t = timer()
    adder_cython(a, b)
    subtractor_cython(a, b)
    return f"Cython took {timer()-t} seconds."


def with_python(a: int, b: int):
    t = timer()
    adder_py(a, b)
    subtractor_py(a, b)
    return f"Python took {timer()-t} seconds."


if __name__ == "__main__":
    """
    Python single thread vs Cython multi thread performance
    """
    a, b = 4000000, 1000000
    print(with_cython(a, b))
    print(with_python(a, b))
