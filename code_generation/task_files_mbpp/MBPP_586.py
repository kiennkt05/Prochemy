# MBPP/586
### Completion
def split_Arr(arr, length, split_index):
    # Split the array into two parts
    first_part = arr[:split_index]
    second_part = arr[split_index:length]
    
    # Combine the second part with the first part
    result = second_part + first_part
    return result

# Test the function with the provided assertion
assert split_Arr([12, 10, 5, 6, 52, 36], 6, 2) == [5, 6, 52, 36, 12, 10]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert split_Arr([12,10,5,6,52,36],6,2) == [5,6,52,36,12,10]
    assert split_Arr([1,2,3,4],4,1) == [2,3,4,1]
    assert split_Arr([0,1,2,3,4,5,6,7],8,3) == [3,4,5,6,7,0,1,2]
