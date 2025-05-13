import itertools
import heapq
import operator

from collections import defaultdict
from functools import reduce
from typing import List

from dataclasses import dataclass

@dataclass
class ArrayElement:
    val: int = 0
    arrayIndex: int = 0

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minElements = [ArrayElement(arrays[0][0], 0), ArrayElement(arrays[1][0], 1)]
        maxElements = [ArrayElement(arrays[0][-1], 0), ArrayElement(arrays[1][-1], 1)]

        def sortMins():
            if minElements[0].val > minElements[1].val:
                minElements[0], minElements[1] = minElements[1], minElements[0]

        def sortMaxes():
            if maxElements[0].val < maxElements[1].val:
                maxElements[0], maxElements[1] = maxElements[1], maxElements[0]

        sortMins()
        sortMaxes()

        for i in range(2, len(arrays)):
            if arrays[i][0] < minElements[1].val:
                minElements[1] = ArrayElement(arrays[i][0], i)
                sortMins()

            if arrays[i][-1] > maxElements[1].val:
                maxElements[1] = ArrayElement(arrays[i][-1], i)
                sortMaxes()

        if minElements[0].arrayIndex != maxElements[0].arrayIndex:
            return abs(minElements[0].val - maxElements[0].val)

        firstDiff = abs(minElements[0].val - maxElements[1].val)
        secondDiff = abs(minElements[1].val - maxElements[0].val)

        return max(firstDiff, secondDiff)