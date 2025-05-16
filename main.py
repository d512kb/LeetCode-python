import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        leftSum = 0
        rightSum = sum(nums)
        ans = [0] * sz

        for index, num in enumerate(nums):
            rightSum -= num
            ans[index] = (num * index - leftSum) + (rightSum - num * (sz-index-1))
            leftSum += num

        return ans