def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    return sum(int(char) for char in s)
print(main("12345")) # output : 15 (1+2+3+4+5)