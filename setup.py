
from setuptools import setup, Extension



setup(
    ext_modules=[Extension('spam', sources=['spam.c'])],
    
)