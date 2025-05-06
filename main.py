import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        connections = defaultdict(list)

        for edge in edges:
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])

        ans = 0

        def dfs(n, prev):
            nonlocal ans
            size = 1
            childrenSizes = set()

            for child in connections[n]:
                if child == prev:
                    continue

                childSize = dfs(child, n)
                childrenSizes.add(childSize)
                size += childSize

            if len(childrenSizes) < 2:
                ans += 1

            return size

        dfs(0, 0)

        return ans