# coding:utf-8

import collections

class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        # 方法一 利用库函数
        return [item[0] for item in collections.Counter[nums].most_common(k)]


    # 方法二 堆
    def topKFrequent2(self, nums: list, k: int) -> list:
        from collections import Counter
        import heapq
        lookup = Counter(nums)
        heap = []
        for ky, vl in lookup.items():
            heapq.heappush(heap, [-vl, ky])
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    # 方法三 堆的缩略写法
    def topKFrequent3(self, nums: list, k: int) -> list:
        import heapq
        c = collections.Counter(nums)
        return heapq.nlargest(k, c, key=lambda x: c[x])