def is_multiple(n, m):
    """
        Takes two integer values and returns True
        is n is a multiple of m, that is, n = mi for
        some integer i, and False otherwise.
    """
    if m % n == 0:
        return True
    else:
        return False