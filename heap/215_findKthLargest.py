#  数组中的第K个最大元素

import json
import random
import heapq

class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        # 利用快速排序
        if len(nums) == 0:
            return -1
        res = self.qsort(nums, 0, len(nums)-1)
        return res[len(nums)-k]


    def qsort(self, nums, left, right):
        if left >= right:
            return nums
        key = nums[left]
        low, high = left, right
        while left < right:
            while left < right and nums[right] >= key:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= key:
                left += 1
            nums[right] = nums[left]
        nums[right] = key
        self.qsort(nums, low, left-1)
        self.qsort(nums, left+1, high)
        return nums

    # 快速选择法
    def findKthLargest2(self, nums: list, k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1.move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k):
            """
            Returns the k-th smallest element of list within left..right
            """
            # If the list contains only one element,return that element
            if left == right:
                return nums[left]
            # select a random pivot_index between
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k == pivot_index:
                return nums[k]
            # go left
            elif k < pivot_index:
                return select(left, pivot_index-1, k)
            # go right
            else:
                return select(pivot_index+1, right, k)

        # kth largest is (n-k)th smallest
        return select(0, len(nums)-1, len(nums)-k)

    # 利用大顶堆
    def findKthLargest3(self, nums: list, k: int) -> int:
        return heapq.nlargest(k, nums)[-1]



def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            k = int(line);

            ret = Solution().findKthLargest(nums, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()