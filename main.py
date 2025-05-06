import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if limit * 3 < n:
            return 0

        # nCr with r = 2
        def c(n):
            return n * (n-1) // 2

        # total amount of cases
        ans = c(n+2)

        # is it possible to exceed one limit?
        if limit < n:
            # remove all cases when any of children got candies over the limit, for every child
            # x + y + z = n, but x >= limit + 1, so x + y + z = n - limit - 1, and we should add 2 to n
            ans -= 3 * c(n-limit+1)

        # is it possible to exceed two limits?
        if 2 * limit < n:
            # while removing all cases in the previous step, we also removed cases when any two children exceeded the limits
            # we counted all these cases twice because some x > limit was counted with y > limit, and vice versa, so add them back
            ans += 3 * c(n-2*limit)

        # the cases when all three children exceeded the limits were eliminated by the very first line of the function

        return ans