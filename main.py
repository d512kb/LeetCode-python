import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        sz = len(grid) + 1
        parent = [-1] * sz * sz

        def findParent(n):
            if parent[n] < 0:
                return n

            parent[n] = findParent(parent[n])
            return parent[n]

        def join(a, b):
            a = findParent(a)
            b = findParent(b)

            if a == b:
                return 1

            if a < b:
                parent[a] += parent[b]
                parent[b] = a
            else:
                parent[b] += parent[a]
                parent[a] = b

            return 0

        def getUnionId(row, col):
            return row * sz + col

        for row in range(sz-1):
            join(getUnionId(row, 0), getUnionId(row+1, 0))
            join(getUnionId(row, sz-1), getUnionId(row+1, sz-1))

        for col in range(sz-1):
            join(getUnionId(0, col), getUnionId(0, col+1))
            join(getUnionId(sz-1, col), getUnionId(sz-1, col+1))

        ans = 1

        for row in range(sz-1):
            for col in range(sz-1):
                if grid[row][col] == '/':
                    ans += join(getUnionId(row, col+1), getUnionId(row+1, col))
                elif grid[row][col] == '\\':
                    ans += join(getUnionId(row, col), getUnionId(row+1, col+1))

        return ans