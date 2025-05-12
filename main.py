import itertools
import operator

from collections import defaultdict
from functools import reduce
from typing import List

from dataclasses import dataclass

@dataclass
class PopularCreator:
    totalViews: int = 0
    topVideoViews: int = 0
    topVideoId: str = chr(ord('z')+1)

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        sz = len(creators)

        mostViews = 0
        popularCreators = defaultdict(PopularCreator)

        for i in range(sz):
            creatorId = creators[i]

            popularCreators[creatorId].totalViews += views[i]

            if popularCreators[creatorId].topVideoViews < views[i]:
                popularCreators[creatorId].topVideoViews = views[i]
                popularCreators[creatorId].topVideoId = ids[i]
            elif popularCreators[creatorId].topVideoViews == views[i] and ids[i] < popularCreators[creatorId].topVideoId:
                popularCreators[creatorId].topVideoId = ids[i]

            if popularCreators[creatorId].totalViews > mostViews:
                mostViews = popularCreators[creatorId].totalViews

        ans = []

        for id, creator in popularCreators.items():
            if creator.totalViews == mostViews:
                ans.append([id, creator.topVideoId])

        return ans