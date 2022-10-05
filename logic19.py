from msvcrt import kbhit


def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    a=x 
    x1 = x % 10
    x //= 10
    
    x2 = x % 10
    x //= 10

    x3 = x % 10
    x //= 10

    n = x1 * 100 + x2 * 10 + x3 
    return n==a 
print(main(999))