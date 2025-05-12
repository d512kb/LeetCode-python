import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rowSwaps = 0
        colSwaps = 0

        for row in range(rows):
            for col in range(cols // 2):
                if grid[row][col] != grid[row][cols-col-1]:
                    rowSwaps += 1

        for col in range(cols):
            for row in range(rows // 2):
                if grid[row][col] != grid[rows-row-1][col]:
                    colSwaps += 1

        return min(rowSwaps, colSwaps)