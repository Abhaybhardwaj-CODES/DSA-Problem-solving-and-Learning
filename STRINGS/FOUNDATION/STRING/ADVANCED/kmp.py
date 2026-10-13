def build_lps(sub):
    """
    Builds the Longest Prefix which is also a Suffix (LPS) array.
    """
    m = len(sub)
    lps = [0] * m
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < m:
        if sub[i] == sub[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(s, sub):
    """
    Checks if 'sub' is present in 's' using the KMP algorithm.
    Returns True if found, False otherwise.
    """
    n = len(s)
    m = len(sub)

    if m == 0:
        return True  # An empty string is always a substring

    # Preprocess the pattern to get the LPS array
    lps = build_lps(sub)

    i = 0  # Index for s
    j = 0  # Index for sub

    while i < n:
        if sub[j] == s[i]:
            i += 1
            j += 1

        if j == m:
            return True  # Substring found!
            # To find more matches, you would do: j = lps[j - 1]

        # Mismatch after j matches
        elif i < n and sub[j] != s[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False


# Example usage:
s = "Hello, welcome to the world of Python programming."
sub = "Python"
result = kmp_search(s, sub)
print(f"Is '{sub}' a substring? {result}")
