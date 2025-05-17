import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = i

        for i in range(2, n//2):
            ops = dp[i] + 2

            for multIndex in range(2*i, n+1, i):
                dp[multIndex] = ops
                ops += 1

        return dp[-1]