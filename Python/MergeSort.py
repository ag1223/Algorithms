'''

introduction:   归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。

step:   1.先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
        然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
        2.再考虑递归分解，基本思路是将数组分解成left和right，如果这两个数组内部数据是有序的，
        那么就可以用上面合并数组的方法将这两个数组合并排序。
        3.如何让这两个数组内部是有序的？可以再二分，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。
        然后合并排序相邻二个小组即可

date:   2018-10-21

'''


def merge(left, right):
    # 合并的过程，将两个有序的数组按照大小分别排序合并

    l, r = 0, 0  # 左右两个数组的下标，设置为0
    result = []  # 设置一个空的用来存放排序合并后的数组
    while l < len(left) and r < len(right):  # 当左右两个数组任意之一都还有元素时
        if left[l] < right[r]:  # 依次比较左右两边的数组元素大小，并添加到result中
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]  # 当循环结束也就是有一个数组已经被取空时，将两个数组剩下的元素添加到result后面
    result += right[r:]  # 当然，其中有一个数组已经是空的了
    return result  # 返回结果


def mergeSort(arr):
    if len(arr) <= 1:  # 当数组只有一个元素的时候，返回数组
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])  # 递归地将数组往下二分到只剩下一个元素
    right = mergeSort(arr[mid:])
    return merge(left, right)  # 然后进行往上合并


if __name__ == '__main__':
    arr1 = [9, 7, 8, 12, 5, 6, 1, 4]
    print(mergeSort(arr1))
