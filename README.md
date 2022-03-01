# RELEASE THE GIL

-----------------------------------------------------------------------------------

**Python is a great language 😃, but the GIL (Global Interpreter Lock) is a huge**
**bottleneck 😢. It's a lock that is held by the interpreter while executing any Python code. This**
**means that if you have a bunch of Python threads running, they all will have to**
**wait for the GIL to be released. This can be a problem, because the GIL is**
**held for a long time, which can lead to many performance issues.**

**The GIL is released whenever a thread is ready to run, and it's held back**
**until all threads are ready to run. This means that if you have a bunch of**
**Python threads running, they'll all be waiting for the GIL to be released**
**but they'll all be blocked still after release. So, even though the threads will run concurrently,**
**only one thread will be allowed to run at the exact same time.**

As you see, there are no way to get rid of the GIL from Python Interpreters.
But, in this project you'll see I've used Cython to run Python code in multi-core CPUs to get its maximum benefit of getting better performance.

To compile Cython code, make sure you have Python installed on your machine and you need Unix-like(Linux/Mac) environment.
For windows, you can use Git Bash or WSL to get the Unix-like environment to compile.

To compile Cython code, run the following command:

```bash
    #!/bin/bash
    $ make
```

or,

```bash
    #!/bin/bash
    $ make build
```

To run tests, run the following command:

```bash
    #!/bin/bash
    $ make test
```

And, to clean up the Cython build, run the following command:

```bash
    #!/bin/bash
    $ make clean
```

## You may ask, why Python intepreter has this GIL?

Ans: The main Python implementation(CPython) is written in C, and many C codes are not thread safe.
Everything are objects in Python, garbage collection are done using reference counting. The big problem
is if one thread(let's say first) that is tracing the reference count of an object, if any other thread(let's say second)
deletes that same object, the first thread will have no idea that same object is deleted by other thread. That's because
reference counting is always done by per thread basis. And also, there may be some situation if one thread may wait for some other
threads which already finished its work, that's called deadlock.
If all threads are accessing the same object and changing at the same time, it may lead to race condtions.
To prevent deadlock or race conditions, there's some locks needed per thread basis which can protect their resources.

Note that, in Java or C#, garbage collection is done by tracing garbage collection, which are aware always of the threads, and
provides atomicity.

## What is the benefit of the GIL?

Ans: The following reasons are:

1. It's easy to write C extensions in Python and provides better C API rather than many popular languages like Java or C#.
2. GIL makes single threaded programs faster.
3. CPython Interpreter loading time is faster than JVM loading time because of GIL.
4. Developers don't have to worry about thread-safety, because GIL always provides thread safety.

## But, the big question is: How can we get rid of the GIL for getting performance?

Ans: As a Python coder, you should always be aware of the performance you're getting from code, and the GIL.
Although, there are multiple ways we can get rid of this. Those are:

1. Using numpy arrays for fast computation or some other good libraries which provides C API.
2. Using Cython or Numba, although Cython is preferred.
3. Using OpenMP API for Python.
4. Using Pybind11 if you are good enough to write C++ code.
5. If you're not satisfied with all I've mentioned, you can write raw C code provided Python C API.

In this repo, you will see how to release the GIL using Cython.

Note that, Python functions are made in such a way, that those can release the GIL when it's I/O bound. Such as:

1. While reading from a file, or writing to a file.
2. While reading from a socket, or writing to a socket.
3. While reading from a database, or writing to a database.
4. While getting data from internet, or sending to a intenet.
5. While sleeping for some time.

In those cases, for I/O bound tasks you can use `threading` module. And, for long running I/O bound tasks, it is
recommended to use `async/await(coroutines)` syntax for better performance.

If don't need threads to run in parallel, you can use `multiprocessing` module. Running tasks in separate processes
won't be any problem for the GIL because every process has their own interpreter, which are again locked by the GIL.

## Which Python interpreter don't have the GIL?

Ans: Jython and IronPython don't have the GIL because they are implemented to run in JVM and .NET environment respectively.
PyPy has the GIL but PyPy-STM(Software Transactional Memory) doesn't have the GIL.

## References

You can know more about this topic which I mentioned below:

1. [Python's Infamous GIL - Larry Hastings](https://www.youtube.com/watch?v=sxMl4DsYgpw)
2. [The Gilectomy project - Larry Hastings](https://www.youtube.com/watch?v=4zeHStBowEk)
3. [Inside the Python GIL - David Beazley](https://www.youtube.com/watch?v=ph374fJqFPE&t=20s)

Happy Coding! 😊
