import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        minVal = maxVal = 0
        prevMax = 0

        for n in nums:
            if n.bit_count() == minVal.bit_count():
                minVal = min(minVal, n)
                maxVal = max(maxVal, n)
            else:
                if prevMax > minVal:
                    return False

                prevMax = maxVal
                minVal = n
                maxVal = n

        if prevMax > minVal:
            return False

        return True