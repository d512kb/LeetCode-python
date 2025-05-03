import operator

from collections import defaultdict
from functools import reduce
from itertools import combinations
from typing import List

class Codec:
    _longToShort = {}
    _shortToLong = {}
    _currentId = 0
    _charSet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _maxChar = len(_charSet)

    def encode(self, longUrl: str) -> str:
        if (longUrl in self._longToShort):
            return self._longToShort[longUrl]

        hash = self._generateHash(longUrl)

        self._longToShort[longUrl] = hash
        self._shortToLong[hash] = longUrl

        return hash


    def decode(self, shortUrl: str) -> str:
        return self._shortToLong[shortUrl]

    def _generateHash(self, longUrl):
        self._currentId += 1
        id = self._currentId
        hash = []

        while id != 0:
            hash.append(self._charSet[id % self._maxChar])
            id = id // self._maxChar

        return ''.join(hash)