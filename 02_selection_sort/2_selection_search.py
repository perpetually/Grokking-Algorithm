# 选择排序
def find_smallest(arr):
    small = arr[0]
    for i in range(len(arr)):
        if arr[i] < small:
            small = arr[i]
    return small


def select_sort(arr):
    result = []
    for i in range(len(arr)):
        small = find_smallest(arr)
        result.append(small)
        arr.remove(small)
    return result


arr = [3, 1, 5, 2, 9, 6]

print(select_sort(arr))

# 时间复杂度f(n)=O(n^2)
# 计算机内存就像是抽屉,需要存储一个对象时给你分配一个内存地址，需要多个时可以使用链表或者数组
# 链表优点是写入删除速度快f(n)= O(1)，而读取速度慢f(n)= O(n)，数组正好相反



