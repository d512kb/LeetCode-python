import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        sz = len(nums)
        conseq = 1
        ans = []

        for i in range(sz):
            if i > 0 and nums[i]-nums[i-1] == 1:
                conseq += 1
            else:
                conseq = 1

            if i+1 >= k:
                ans.append(nums[i] if conseq >= k else -1)

        return ans