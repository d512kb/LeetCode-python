import copy
import itertools
import heapq
import operator

from collections import defaultdict
from collections import deque
from dataclasses import dataclass
from functools import reduce
from typing import List

class Node:
    def __init__(self):
        self.word = False
        self.children = {}

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        sz = len(s)
        dp = [0] * (sz + 1)
        root = Node()

        for word in dictionary:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]

            node.word = True

        for n in range(sz-1, -1, -1):
            node = root
            dp[n] = 1 + dp[n+1]

            for i in range(n, sz):
                if s[i] not in node.children:
                    break

                node = node.children[s[i]]
                if node.word:
                    dp[n] = min(dp[n], dp[i+1])

        return dp[0]