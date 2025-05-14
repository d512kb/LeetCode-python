import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0

        for i in range(1, n+1):
            ans = (ans + k) % i

        return ans + 1