import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        # squares can't affect the div by 4 rule so just count ans
        for row in range(rows // 2):
            for col in range(cols // 2):
                ones = grid[row][col] + grid[row][cols-col-1] + grid[rows-row-1][col] + grid[rows-row-1][cols-col-1]
                ans += min(ones, 4-ones)

        ones = 0
        oddPairs = 0

        if rows % 2 == 1:
            row = rows // 2

            for col in range(cols // 2):
                onesPair = grid[row][col] + grid[row][cols-col-1]
                oddPairs += onesPair % 2
                ones += onesPair // 2 * 2

        if cols % 2 == 1:
            col = cols // 2

            for row in range(rows // 2):
                onesPair = grid[row][col] + grid[rows-row-1][col]
                oddPairs += onesPair % 2
                ones += onesPair // 2 * 2

        if rows % 2 == 1 and cols % 2 == 1:
            ans += grid[rows // 2][cols // 2]

        ans += oddPairs

        if ones % 4 == 2 and oddPairs == 0:
            ans += 2

        return ans