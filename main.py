import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = [1]
        i2 = i3 = i5 = 0

        for _ in range(1, n):
            ug1 = uglyNumbers[i2]*2
            ug2 = uglyNumbers[i3]*3
            ug3 = uglyNumbers[i5]*5

            ug = min(ug1, ug2, ug3)
            uglyNumbers.append(ug)

            if ug == ug1:
                i2 += 1
            if ug == ug2:
                i3 += 1
            if ug == ug3:
                i5 += 1

        return uglyNumbers[-1]