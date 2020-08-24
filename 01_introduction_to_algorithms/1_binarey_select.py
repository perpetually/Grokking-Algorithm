# 二分查找
def binarey(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        index = (low + high) // 2
        mid = arr[index]

        if mid == item:

            return index
        elif mid > item:
            low = mid + 1

        else:
            high = mid - 1



arr = [3, 1, 6, 2, 9, 7]
item = 6

print(binarey(arr, 6))

# 时间复杂度为f(n)=O(log n)
# 1需要列表有序
# 2查询数量越多速度优势越快
