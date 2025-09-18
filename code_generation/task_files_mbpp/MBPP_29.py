# MBPP/29
### Completion
def get_Odd_Occurrence(arr, n):
    count = {}
    
    # Count occurrences of each element
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    # Find the element with an odd count
    for num, cnt in count.items():
        if cnt % 2 != 0:
            return num
            
    return None  # Return None if no odd occurrence is found

# Test the function with the provided assertion
assert get_Odd_Occurrence([1, 2, 3, 1, 2, 3, 1], 7) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Odd_Occurrence([1,2,3,1,2,3,1],7) == 1
    assert get_Odd_Occurrence([1,2,3,2,3,1,3],7) == 3
    assert get_Odd_Occurrence([2,3,5,4,5,2,4,3,5,2,4,4,2],13) == 5
