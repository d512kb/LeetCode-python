import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        lastMask = n-1

        for pos in range(64):
            if (x & (1 << pos)):
                continue

            x |= (lastMask & 1) << pos
            lastMask >>= 1

        return x