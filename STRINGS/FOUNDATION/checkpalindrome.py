def is_palindrome(string):
    """
    Checks if the given string is a palindrome.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]
string = "A man, a plan, a canal: Panama"
if is_palindrome(string):   
    print(f'"{string}" is a palindrome.')