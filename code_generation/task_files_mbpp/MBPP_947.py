# MBPP/947
### Completion
def len_log(words):
    if not words:
        return 0  # Return 0 if the list is empty
    return min(len(word) for word in words)

# Example usage
assert len_log(["win", "lose", "great"]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert len_log(["win","lose","great"]) == 3
    assert len_log(["a","ab","abc"]) == 1
    assert len_log(["12","12","1234"]) == 2
