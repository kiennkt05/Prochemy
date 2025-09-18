# MBPP/157
### Completion
def encode_list(lst):
    if not lst:
        return []
    
    encoded = []
    count = 1
    previous = lst[0]
    
    for current in lst[1:]:
        if current == previous:
            count += 1
        else:
            encoded.append([count, previous])
            previous = current
            count = 1
            
    # Append the last counted element
    encoded.append([count, previous])
    
    return encoded

# Test the function with the provided assertion
assert encode_list([1, 1, 2, 3, 4, 4.3, 5, 1]) == [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert encode_list([1,1,2,3,4,4.3,5,1])==[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
    assert encode_list('automatically')==[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
    assert encode_list('python')==[[1, 'p'], [1, 'y'], [1, 't'], [1, 'h'], [1, 'o'], [1, 'n']]
