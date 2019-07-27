# multiple passes
# only one exchange on each pass
# looks for the largest value as it makes a pass and,
#   after completing the pass, places it in the proper location.

def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[positionOfMax], alist[fillslot] = alist[fillslot], alist[positionOfMax]

alist = [4, 6, 10, 1, 3, 2, 5, 9, 8, 7]
selectionSort(alist)
print('selection sorted list:', alist)