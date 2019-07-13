def reverse_list(seq, n=1):
    """A recursive function to reverse a list."""
    # base case: if the length of the sequence divided by n <= 1
    if len(seq) // n <= 1:
        return seq
    else:
        a = n - 1
        b = len(seq) - n
        # use multiple assignment to swap the values in the list
        seq[a], seq[b] = seq[b], seq[a]
        return reverse_list(seq, n + 1) # n is incremented on each recursive call to move toward the base case


def main():

    reversedList = reverse_list([1, 2, 3, 4, 5, 6, 7, 8])
    print('reversed list:', reversedList)


if __name__ == '__main__': main()