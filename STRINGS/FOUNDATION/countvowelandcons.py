def countvowelandcons(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count
string = "Hello, World!"
vowel_count, consonant_count = countvowelandcons(string)
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)