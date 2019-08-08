import random

lst = [random.randint(1, 10) for i in range(7)]
print('randomly generated list:', lst)


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root,newBranch):
    t = root.pop(1)
    if newBranch < root[0]:
        root[0], newBranch = root[0], newBranch

    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root


def insertRight(root,newBranch):
    t = root.pop(2)
    if newBranch < root[0]:
        root[0], newBranch = root[0], newBranch
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root


def buildTree(root, ls, index):
    insertLeft(root, ls[index])
    insertRight(root, ls[index+1])


def continueLoop(iterations):
    return iterations < len(lst) // 2


tree = BinaryTree(lst[0])
branch = 0
l1 = list(range(1, len(lst), 2))
while continueLoop(branch):
    if branch == 0:
        buildTree(tree, lst, l1[branch])
    else:
        buildTree(tree[branch], lst, l1[branch])
    branch += 1

print('tree heap:', tree)


class HeapList:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[1 * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        self.heapList = self.heapList[1:]


heapList = HeapList()
heapList.buildHeap(lst)
print('list heap:', heapList.heapList)


#          X
#      /       \
#     X         X
#    / \       / \
#   X   X     X   X