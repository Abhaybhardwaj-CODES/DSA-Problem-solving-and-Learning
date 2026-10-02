def  reverse (string):
    """
    Reverses the given string.

    Args:
        string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return string[::-1]
string = "Hello, World!"
reversed_string = reverse(string)
print(reversed_string)  # Output: !dlroW ,olleH