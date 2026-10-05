def group_anagrams(strs):
    """
    Groups anagrams from a list of strings.

    Args:
        strs (List[str]): A list of strings.

    Returns:
        List[List[str]]: A list of lists, where each inner list contains anagrams.
    """
    anagram_groups = {}

    for s in strs:
        # Sort the characters in the string to create a key
        sorted_str = ''.join(sorted(s))
        
        # Add the string to its anagram group
        if sorted_str in anagram_groups:
            anagram_groups[sorted_str].append(s)
        else:
            anagram_groups[sorted_str] = [s]

    # Return all the anagram groups
    return list(anagram_groups.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]