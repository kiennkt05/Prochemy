# MBPP/570
### Completion
def remove_words(strings, to_remove):
    # Create a set of characters/substrings to remove for faster lookup
    to_remove_set = set(to_remove)
    
    # Function to remove unwanted characters/substrings from a single string
    def clean_string(s):
        for item in to_remove_set:
            s = s.replace(item, '')
        return s.strip()  # Remove leading/trailing whitespace

    # Apply the clean_string function to each string in the list
    return [clean_string(s) for s in strings]

# Test the function with the provided assertion
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
