# 选择排序
'''

introduction:   选择排序无疑是最简单直观的排序。它的工作原理如下。

step:   1.在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
        2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
        3.以此类推，直到所有元素均排序完毕。

date:   2018-10-17

'''


def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i  # 每次循环设置初始最小值的索引
        for j in range(i + 1, len(arr)):  # 从初始最小值后面循环
            if arr[j] < arr[minIndex]:  # 如果比初始最小值小
                minIndex = j  # 更新最小索引
        if minIndex != i:  # 内循环进行一次后最小索引如果变了，就交换值。
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
            print(arr)  # 每交换一次，输出一下当前数组顺序
    print("Final result:\n", arr)


if __name__ == '__main__':
    arr1 = [9, 7, 8, 12, 5, 6, 1, 4]
    selectionSort(arr1)
