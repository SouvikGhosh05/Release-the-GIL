from cython.parallel cimport parallel
from cython.parallel import prange
cimport openmp
import cython

cdef extern from "adder.c" nogil:       #'nogil' flag is needed to run in 'with nogil' context
    long long adder_fromc(long long a, long long b)

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef long long adder_py(long long ac, long long bc):
    
    cdef:
        long long a= ac
        long long b= bc
        long long add
        int num_threads

    openmp.omp_set_dynamic(1)
    with nogil, parallel():             # It allows to run with parallel in other threads
        num_threads = openmp.omp_get_num_threads()
        add= adder_fromc(a,b)
        with gil:
            return add

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef long long subtractor_py(long long int a, long long int b):

    cdef:
        long long int ac=a
        long long int bc=b
        long long int i
    
    for i in prange(bc, nogil=True):    #releases GIL and runs in parallel
        ac-=i
    return ac