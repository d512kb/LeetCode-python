import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        rows = len(mat)

        for r in mat:
            r.sort()

        possible_sums = {0}

        for row in mat:
            next_sums = set()
            for val in row:
                for s in possible_sums:
                    next_sums.add(s + val)
                if val > target:
                    break
            possible_sums = next_sums

        return min(abs(s - target) for s in possible_sums)