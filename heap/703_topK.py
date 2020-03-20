# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
import heapq

class KthLargest:

    def __init__(self, k: int, nums: list):
        self.k = k
        self.nums = nums


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]
    
    # 堆方法实现
    def add2(self, val: int) -> int:
        self.nums.append(val)
        return heapq.nlargest(self.k, self.nums)[-1]
k=3

if __name__ == '__main__':
    k = KthLargest(k, [4,5,8,2])
    print(k.add(3))