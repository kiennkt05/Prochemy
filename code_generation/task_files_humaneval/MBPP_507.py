# MBPP/507
### Completion
def remove_words(original_list, words_to_remove):
    """
    Remove specific words from the original list.

    Parameters:
    original_list (list): The list of words from which to remove words.
    words_to_remove (list): The list of words to be removed from the original list.

    Returns:
    list: A new list with the specified words removed.
    """
    # Create a new list excluding the words to remove
    filtered_list = [word for word in original_list if word not in words_to_remove]
    return filtered_list

# Test case
assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'], ['white', 'orange']) == ['red', 'green', 'blue', 'black']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['white', 'orange'])==['red', 'green', 'blue', 'black']
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['black', 'orange'])==['red', 'green', 'blue', 'white']
    assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['blue', 'white'])==['red', 'green', 'black', 'orange']
