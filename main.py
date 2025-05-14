import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def lastRemaining(self, n: int) -> int:
        left = 1
        step = 1
        ltr = True

        while n > 1:
            if ltr or n % 2 == 1:
                left += step

            n >>= 1
            step <<= 1
            ltr = not ltr

        return left