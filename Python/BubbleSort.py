'''

introduction:   冒泡排序的原理非常简单，它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

step:   比较相邻的元素。如果第一个比第二个大，就交换他们两个。
        对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
        针对所有的元素重复以上的步骤，除了最后一个。
        持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

date:   2018-10-17

'''


def bubbleSort(arr):
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break
        print(arr)
    print("Final result:\n", arr)


if __name__ == '__main__':
    arr1 = [9, 7, 8, 12, 5, 6, 1, 4]
    bubbleSort(arr1)
