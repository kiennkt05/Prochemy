# MBPP/898
### Completion
def extract_elements(lst, n):
    if n <= 0:
        return []
    
    result = []
    previous = None
    count = 0
    
    for element in lst:
        if element != previous:
            if count > 0:
                result.append(previous)
            previous = element
            count = 1
        else:
            count += 1
        
        if len(result) == n:
            break
    
    if count > 0 and len(result) < n:
        result.append(previous)
    
    return result

# Test the function with the provided assertion
assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7], 2) == [1, 4]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7],2)==[1, 4]
    assert extract_elements([0, 1, 2, 3, 4, 4, 4, 4, 5, 7],4)==[4]
    assert extract_elements([0,0,0,0,0],5)==[0]
