# MBPP/570
### Completion
def remove_words(strings, to_remove):
    """
    Remove specified words or characters from a list of strings.

    Parameters:
    strings (list of str): The list of strings to process.
    to_remove (list of str): The list of words or characters to remove from the strings.

    Returns:
    list of str: A new list of strings with the specified words or characters removed.
    """
    cleaned_strings = []
    
    for string in strings:
        # Remove each word/character in to_remove from the current string
        for word in to_remove:
            string = string.replace(word, '')
        cleaned_strings.append(string.strip())  # Strip leading/trailing whitespace
    
    return cleaned_strings

# Test case
assert remove_words(['Red color', 'Orange#', 'Green', 'Orange @', "White"], ['#', 'color', '@']) == ['Red', '', 'Green', 'Orange', 'White']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_words(['Red color', 'Orange#', 'Green', 'Orange @', "White"],['#', 'color', '@'])==['Red', '', 'Green', 'Orange', 'White']
    assert remove_words(['Red &', 'Orange+', 'Green', 'Orange @', 'White'],['&', '+', '@'])==['Red', '', 'Green', 'Orange', 'White']
    assert remove_words(['Red &', 'Orange+', 'Green', 'Orange @', 'White'],['@'])==['Red &', 'Orange+', 'Green', 'Orange', 'White']
