def str_compression(s):
    """
    Compresses a string by replacing sequences of the same character with that character followed by the count of repetitions.
    
    Args:
    s (str): The input string to be compressed.
    
    Returns:
    str: The compressed string.
    """
    if not s:
        return ""
    
    compressed = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
            
    # Append the last character and its count
    compressed.append(s[-1] + str(count))
    
    return ''.join(compressed)
s = "aaabbccccdaa"
print(str_compression(s))  # Output: "a3b2c4d1a2"