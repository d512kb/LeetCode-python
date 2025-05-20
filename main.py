import copy
import itertools
import heapq
import operator

from collections import defaultdict
from collections import deque
from dataclasses import dataclass
from functools import reduce
from math import inf
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        tree = defaultdict(list)

        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])

        visited = [False] * len(amount)
        bobTimings = {}

        def buildPathToBob(node, time):
            visited[node] = True
            bobTimings[node] = time

            if node == 0:
                return True

            for nextNode in tree[node]:
                if visited[nextNode]:
                    continue

                if buildPathToBob(nextNode, time+1):
                    return True

            bobTimings.pop(node)

            return False

        buildPathToBob(bob, 0)

        visited = [False] * len(amount)
        ans = -inf

        def explorePaths(node, profit, time):
            nonlocal ans
            visited[node] = True

            if node not in bobTimings or time < bobTimings[node]:
                profit += amount[node]
            elif time == bobTimings[node]:
                profit += amount[node] // 2

            lastNode = True

            for nextNode in tree[node]:
                if visited[nextNode]:
                    continue

                lastNode = False

                explorePaths(nextNode, profit, time+1)

            if lastNode:
                ans = max(ans, profit)

        explorePaths(0, 0, 0)

        return int(ans)