import operator

from collections import defaultdict
from functools import reduce
from itertools import combinations
from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        totalXor = 0
        maxK = (1 << maximumBit) - 1
        result = []

        for n in nums:
            totalXor ^= n
            result.append(~totalXor & maxK)

        return result[::-1]