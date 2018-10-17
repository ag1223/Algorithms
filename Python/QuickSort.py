'''

introduction:   快速排序是冒泡排序的一种改进,采用分而治之和递归的方法

step:   1.从数列中挑出一个元素作为基准数。
        2.分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
        3.再对左右区间递归执行第二步，直至各区间只有一个数。

date:   2018-10-17

'''


def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [y for y in arr if y == pivot]
        greater = [z for z in arr if z > pivot]
    return quickSort(less) + equal + quickSort(greater)


if __name__ == '__main__':
    arr1 = [9, 7, 8, 12, 5, 6, 1, 4]
    print(quickSort(arr1))
