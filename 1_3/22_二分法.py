# 二分法
# 在一个有序的数列里
# 每次都能够排除掉一半的数据
lst = [1, 3, 45, 53, 65, 89, 613]

n = int(input(">>>>:"))

left = 0
right = len(lst) - 1 # 最大的索引

# while left <= right:
#     mid = (left + right) // 2 # 计算中间位置的索引
#     if n > lst[mid]:
#         left = mid + 1
#     elif n < lst[mid]:
#         right = mid - 1
#     else:
#         print('找到数据了，位置是', mid)
#         break
# else:
#     print('没有找到数据')


# 递归版本
def find(lst, n, left, right):
    if left > right:
        print('没找到')
        return
    mid = (left + right) // 2
    if n > lst[mid]:
        left = mid + 1
    elif n < lst[mid]:
        right = mid - 1
    else:
        print('找到了，位置', mid)
        return
    find(lst, n, left, right) # 递归查找

find(lst, n, left, right)
