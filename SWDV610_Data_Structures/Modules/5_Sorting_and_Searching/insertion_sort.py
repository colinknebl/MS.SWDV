# maintains a sorted sublist in the lower positions of the list
# Each new item is then “inserted” back into the previous sublist
#   such that the sorted sublist is one item larger

def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue

alist = [4, 6, 10, 1, 3, 2, 5, 9, 8, 7]
insertionSort(alist)
print('insertion sorted list:', alist)