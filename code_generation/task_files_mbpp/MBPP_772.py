# MBPP/772
### Completion
def remove_length(input_string, k):
    # Split the input string into words
    words = input_string.split()
    # Filter out words that have length k
    filtered_words = [word for word in words if len(word) != k]
    # Join the filtered words back into a string
    return ' '.join(filtered_words)

# Test the function with the provided assertion
assert remove_length('The person is most value tet', 3) == 'person is most value'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_length('The person is most value tet', 3) == 'person is most value'
    assert remove_length('If you told me about this ok', 4) == 'If you me about ok'
    assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'
