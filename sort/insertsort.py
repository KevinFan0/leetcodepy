# 直接插入排序
# 稳定算法，即排序时相等的两个数不会交换位置
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j > 0:
            if arr[j] > key:
                arr[j+1] = arr[j]
                arr[j] = key
            j -= 1
    return arr


# 希尔排序
# 非稳定算法
def shell_sort(arr):
    count = len(arr)
    step = 2
    group = count / step
    while group > 0:
        for i in range(group):
            j = i + group
            while j < count:
                k = j - group
                key = arr[j]
                while k >= 0:
                    if arr[k] > key:
                        arr[k+group] = arr[k]
                        arr[k] = key
                    k -= group
                j += group
        group /= step
    return arr


# 冒泡排序
# 非稳定算法
def bubble_sort(arr):
    count = len(arr)
    for i in range(count):
        for j in range(i+1, count):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# 选择排序
def select_sort(arr):
    for i in range(len(arr)):
        arr[i] = min(arr[i:])
    return arr

def select_sort2(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr


# 快速排序
# 不稳定 n*logn
def quick_sort(arr, left, right):
    if left >= right:
        return arr
    key = arr[left]
    low, high = left, right
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]
    arr[right] = key
    quick_sort(arr, low, left-1)
    quick_sort(arr, left+1, high)
    return arr


# 归并排序
# 稳定 n*logn 需要额外的O(n)空间
def merge(left: list, right: list) -> list:
    # 合并过程
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(lists: list) -> list:
    if len(lists) <= 1:
        return lists
    mid = len(lists) / 2
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    return merge(left, right)



if __name__ == '__main__':
    arr = [3, 4, 2, 14, 55,23,34,7]
    print(select_sort2(arr))