# MBPP/275
### Completion
def get_Position(arr, element, count):
    # Initialize the last position to -1 (not found)
    last_position = -1
    
    # Iterate through the array to find the last occurrence of the element
    for i in range(len(arr)):
        if arr[i] == element:
            last_position = i
    
    # If the element was found, we need to check how many times we can remove it
    if last_position != -1:
        # If count is greater than the number of occurrences, adjust it
        occurrences = arr.count(element)
        if count > occurrences:
            count = occurrences
        
        # Calculate the last position after removing the specified count
        for _ in range(count):
            # Remove the last occurrence of the element
            arr.pop(last_position)
            # Recalculate the last position
            last_position = -1
            for i in range(len(arr)):
                if arr[i] == element:
                    last_position = i
    
    return last_position

# Test the function with the provided assertion
assert get_Position([2, 5, 4], 3, 2) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Position([2,5,4],3,2) == 2
    assert get_Position([4,3],2,2) == 2
    assert get_Position([1,2,3,4],4,1) == 4
