def removedupli(string):
    """
    Remove duplicates from a string while preserving the order of characters.

    Parameters:
    string (str): The input string from which duplicates need to be removed.

    Returns:
    str: A new string with duplicates removed, preserving the original order.
    """
    seen = set()
    result = []
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)  
string = "programming"
result = removedupli(string)
print(result)  # Output: "progamin"