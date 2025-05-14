import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        subarr = defaultdict(int)
        subarrSum = 0
        duplicates = 0

        for i in range(k):
            subarrSum += nums[i]
            subarr[nums[i]] += 1

            if subarr[nums[i]] == 2:
                duplicates += 1

        if duplicates == 0:
            ans = subarrSum

        for i in range(k, len(nums)):
            aNum = nums[i-k]
            bNum = nums[i]

            subarrSum -= aNum
            subarr[aNum] -= 1
            if subarr[aNum] == 1:
                duplicates -= 1

            subarrSum += bNum
            subarr[bNum] += 1
            if subarr[bNum] == 2:
                duplicates += 1

            if duplicates == 0:
                ans = max(ans, subarrSum)

        return ans