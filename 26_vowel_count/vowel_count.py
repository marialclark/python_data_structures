VOWELS = set("aeiou")

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase2 = phrase.lower()
    vowel_count = {}

    for ltr in phrase2:
        if ltr in VOWELS:
            vowel_count[ltr] = vowel_count.get(ltr, 0) + 1
    return vowel_count