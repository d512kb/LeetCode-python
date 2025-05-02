import operator

from collections import defaultdict
from functools import reduce
from itertools import combinations
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = reduce(operator.or_, nums, 0)
        ans = 0

        def calc(index, num) -> None:
            nonlocal ans

            if (index == len(nums)):
                if (num == maxOr):
                    ans += 1
                return

            calc(index+1, num)
            calc(index+1, num | nums[index])

        calc(0, 0)

        return ans