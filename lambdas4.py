"""Using sorted and lambdas to randomize an iterable"""

from random import random

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sorted_list = sorted(a_list, key=lambda _: random())

print(sorted_list)
