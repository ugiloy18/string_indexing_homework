def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if 0 <= n < len(s):
        return s[n]
    else:
        return False
    print(main("hello", 1)) #output : 'e'
    print(main("hello" , 5)) # output : false
    print(main("hi", -1))
