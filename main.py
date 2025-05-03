import operator

from collections import defaultdict
from functools import reduce
from itertools import combinations
from typing import List

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = [1]
        ans = []
        nextVal = 0;

        for p in pattern:
            if p == 'I':
                nextVal = stack[-1] + 1

                while len(stack) > 0:
                    ans.append(stack[-1])
                    stack.pop()

                stack.append(nextVal)
            else:
                stack.append(stack[-1] + 1)

        while len(stack) > 0:
            ans.append(stack[-1])
            stack.pop()

        return ''.join(map(lambda x: str(x), ans))