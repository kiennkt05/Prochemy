# MBPP/90
### Completion
def len_log(words):
    if not words:  # Check if the list is empty
        return 0
    return max(len(word) for word in words)

# Test the function with the provided assertion
assert len_log(["python", "PHP", "bigdata"]) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert len_log(["python","PHP","bigdata"]) == 7
    assert len_log(["a","ab","abc"]) == 3
    assert len_log(["small","big","tall"]) == 5
