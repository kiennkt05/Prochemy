# MBPP/526
### Completion
def capitalize_first_last_letters(s: str) -> str:
    """
    Capitalizes the first and last letters of each word in the given string.

    Parameters:
    s (str): The input string.

    Returns:
    str: The modified string with first and last letters of each word capitalized.
    """
    # Split the string into words
    words = s.split()
    
    # Process each word
    capitalized_words = []
    for word in words:
        if len(word) > 0:  # Check if the word is not empty
            # Capitalize the first and last letters
            first_letter = word[0].upper()
            last_letter = word[-1].upper() if len(word) > 1 else ''
            middle_part = word[1:-1]  # Get the middle part of the word
            capitalized_word = first_letter + middle_part + last_letter
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append(word)  # Append empty words as is

    # Join the capitalized words back into a single string
    return ' '.join(capitalized_words)

# Test case
assert capitalize_first_last_letters("python") == "PythoN"

# Additional test cases
assert capitalize_first_last_letters("hello world") == "HellO WorlD"
assert capitalize_first_last_letters("a b c") == "A B C"
assert capitalize_first_last_letters("capitalize each word") == "Capitalize EacH WorlD"
assert capitalize_first_last_letters("") == ""  # Edge case for empty string

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert capitalize_first_last_letters("python") == "PythoN"
    assert capitalize_first_last_letters("bigdata") == "BigdatA"
    assert capitalize_first_last_letters("Hadoop") == "HadooP"
