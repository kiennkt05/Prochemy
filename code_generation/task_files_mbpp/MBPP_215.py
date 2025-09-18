# MBPP/215
### Completion
def decode_list(encoded):
    decoded = []
    for item in encoded:
        if isinstance(item, list):
            count, value = item
            decoded.extend([value] * count)
        else:
            decoded.append(item)
    return decoded

# Test the function with the provided assertion
assert decode_list([[2, 1], 2, 3, [2, 4], 5, 1]) == [1, 1, 2, 3, 4, 4, 5, 1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert decode_list([[2, 1], 2, 3, [2, 4], 5,1])==[1,1,2,3,4,4,5,1]
    assert decode_list(['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y'])==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', 'l', 'l', 'y']
    assert decode_list(['p', 'y', 't', 'h', 'o', 'n'])==['p', 'y', 't', 'h', 'o', 'n']
