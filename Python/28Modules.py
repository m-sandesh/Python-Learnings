# A library of useful methods and functions gathered in a single file.

# Methods of importing modules.
# 1
import math as math # Abbreviate a module as a name to use it as object.
# Use:
math.sqrt(10)

# 2
from math import sqrt # Import only required methods and functions from a module. No use of abbreviations if only a method is imported.
# Use:
sqrt(10)

# 3 BEST WAY
# from math import *  # Imports all without needing abbreviations.
# Use:
sqrt(10)


# HAND MADE MODULE IMPORT  # 28Calc.py
import DemoCalcModule as demo   # Commented as modules cannot start with numbers. TO Fix rename file 28Calc.py

demo.addMe(10, 5)
demo.mulMe(10, 10)







