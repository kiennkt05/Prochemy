# MBPP/165
### Completion
def count_char_position(s):
    count = 0
    for index, char in enumerate(s):
        # Calculate the position in the alphabet (1-based)
        position = ord(char.lower()) - ord('a') + 1
        # Check if the position matches the index (1-based)
        if position == index + 1:
            count += 1
    return count

# Test the function with the provided assertion
assert count_char_position("xbcefg") == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5
