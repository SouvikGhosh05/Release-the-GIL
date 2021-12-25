from setuptools import setup, Extension
from Cython.Build import cythonize


sourcefiles = ["src_Cython/add_sub.pyx"]  # Cython file mentioned as source
ext_modules = [
    Extension(
        "add_n_sub",  # Name of the module
        sourcefiles,
        extra_compile_args=["-fopenmp", "-O3"],  # "-O3" for better optimization of gcc
        extra_link_args=["-fopenmp"],
    )
]
setup(
    name="Addition and Subtraction",
    ext_modules=cythonize(ext_modules, annotate=True, language_level="3str"),
    zip_safe=False,
)
