import copy
import itertools
import heapq
import operator

from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import List

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        onesByRow = [0] * rows
        onesByColumn = [0] * cols

        for row in range(rows):
            onesByRow[row] = sum(grid[row])

        for col in range(cols):
            ones = 0
            for row in range(rows):
                ones += grid[row][col]

            onesByColumn[col] = ones

        ans = 0

        for row in range(rows):
            if onesByRow[row] == 0:
                continue

            for col in range(cols):
                if (grid[row][col] == 1):
                    ans += (onesByRow[row]-1) * (onesByColumn[col]-1)

        return ans