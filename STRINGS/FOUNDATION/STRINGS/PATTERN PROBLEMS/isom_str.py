def isom_str(str1, str2):
    """
    Checks if two strings are isomorphic.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if the strings are isomorphic, False otherwise.
    """
    if len(str1) != len(str2):
        return False

    mapping = {}
    used = set()

    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]

        if char1 in mapping:
            if mapping[char1] != char2:
                return False
        else:
            if char2 in used:
                return False
            mapping[char1] = char2
            used.add(char2)

    return True
str1 = "egg"
str2 = "add"
print(isom_str(str1, str2))  # Output: True