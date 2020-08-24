# # O(nlog n)
# def quick_sort(list):
#     if len(list) < 2:
#         return list
#
#     else:
#         # 选择基准条件
#         item = list[0]
#         less = [x for x in list[1:] if x <= item]
#         large = [x for x in list[1:] if x > item]
#         list = quick_sort(less) + [item] + quick_sort(large)
#         return list
#
#
# list = [10, 5, 2, 3]
# print(quick_sort(list))

# 快速排列(f(n)=O(nlogn)
# 1当数组长度小于2就不用再排列了
# 2找到一个基准值,只要比它小的都放在数组左边,大的放在右边
def qucik_sort(arr):
    if len(arr) < 2:
        return arr

    else:
        item = arr[0]
        small = [x for x in arr[1:] if x <= item]
        large = [x for x in arr[1:] if x > item]
        print(item, small, large)

        arr = qucik_sort(small) + [item] + qucik_sort(large)

        return arr


arr = [2, 1, 7, 3, 5, 0]
print(qucik_sort(arr))
