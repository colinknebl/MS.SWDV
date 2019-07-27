# multiple passes over list
# compares adjacent items and exchanges those that are out of order.
# Each pass through the list places the next largest value in its proper place

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

alist = [4, 6, 10, 1, 3, 2, 5, 9, 8, 7]
bubbleSort(alist)
print('bubble sorted list:', alist)