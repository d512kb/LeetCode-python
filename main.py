import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        current = 1

        for _ in range(n):
            # Add the current number to the result list
            ans.append(current)

            # If multiplying by 10 is valid, move to the next lexicographical branch
            if current * 10 <= n:
                current *= 10
            else:
                # Otherwise, backtrack to find the next valid number
                while current % 10 == 9 or current + 1 > n:
                    current //= 10  # Move up one level in the lexicographical tree
                current += 1  # Move to the next number

        # Return the result list
        return ans
