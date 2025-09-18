# MBPP/317
### Completion
def modified_encode(lst):
    if not lst:  # Handle empty list case
        return []
    
    result = []
    count = 1
    current = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] == current:
            count += 1
        else:
            # Append the encoded part
            if count > 1:
                result.append([count, current])
            else:
                result.append(current)
            # Reset for the new element
            current = lst[i]
            count = 1
    
    # Handle the last group
    if count > 1:
        result.append([count, current])
    else:
        result.append(current)
    
    return result

# Test case
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
