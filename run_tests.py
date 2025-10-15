import unittest

from tests.homework.e_functions import (tests_functions)

suite = unittest.TestLoader().discover('tests/homework/e_functions')
unittest.TextTestRunner().run(suite)
# /src/homework/e_functions/void_func.py