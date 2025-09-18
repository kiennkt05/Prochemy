# MBPP/317
### Completion
def modified_encode(lst):
    if not lst:
        return []
    
    encoded = []
    count = 1
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            if count > 1:
                encoded.append([count, lst[i - 1]])
            else:
                encoded.append(lst[i - 1])
            count = 1
    
    # Handle the last group
    if count > 1:
        encoded.append([count, lst[-1]])
    else:
        encoded.append(lst[-1])
    
    return encoded

# Test the function with the provided assertion
assert modified_encode([1, 1, 2, 3, 4, 4, 5, 1]) == [[2, 1], 2, 3, [2, 4], 5, 1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert modified_encode([1,1,2,3,4,4,5,1])==[[2, 1], 2, 3, [2, 4], 5, 1]
    assert modified_encode('automatically')==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y']
    assert modified_encode('python')==['p', 'y', 't', 'h', 'o', 'n']
