'''

introduction:   直接插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

step:   1.从第一个元素开始，该元素可以认为已经被排序
        2.取出下一个元素，在已经排序的元素序列中从后向前扫描
        3.如果被扫描的元素（已排序）大于新元素，将该元素后移一位
        4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
        5.将新元素插入到该位置后
        6.重复步骤2~5

date:   2018-10-17

'''


def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        index = i
        while index > 0:
            if key < arr[index - 1]:
                arr[index] = arr[index - 1]
                index -= 1
            else:
                break
        arr[index] = key
        print(arr)
    print("Final result:\n", arr)


if __name__ == '__main__':
    arr1 = [9, 7, 8, 12, 5, 6, 1, 4]
    insertSort(arr1)
