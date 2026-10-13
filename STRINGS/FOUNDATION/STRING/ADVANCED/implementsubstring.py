def implementsubstring(s, sub):
    """
    Check if the substring 'sub' is present in the string 's'.

    Parameters:
    s (str): The main string to search within.
    sub (str): The substring to search for.

    Returns:
    bool: True if 'sub' is found in 's', False otherwise.
    """
    return sub in s
s = "Hello, welcome to the world of Python programming."
sub = "Python"
result = implementsubstring(s, sub)
print(f"Is '{sub}' a substring of the main string? {result}")