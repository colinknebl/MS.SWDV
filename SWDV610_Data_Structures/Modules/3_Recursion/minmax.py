def minmax(seq):
    return _minmax(seq, seq[0], seq[0])


def _minmax(seq, _min, _max, n=0):
    """
    A short recursive Python function that finds the minimum and
    maximum values in a sequence without using any loops.
    """
    # base case: if n is equal to the length of the list
    if n == len(seq):
        return (_min, _max)
    else:
        if _min > seq[n]:
            _min = seq[n]
        if _max < seq[n]:
            _max = seq[n]
        return _minmax(seq, _min, _max, n + 1) # n is incremented by one on each recursive call to move toward the base case


def main():
    seq = [85, 44, 0, 67, 9, 123, 5, 15, 1]

    minimum, maximum = minmax(seq)
    print('min = {} :: max = {}'.format(minimum, maximum))


if __name__ == '__main__': main()