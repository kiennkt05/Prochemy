# MBPP/819
### Completion
def count_duplic(numbers):
    if not numbers:
        return [], []
    
    unique_elements = []
    counts = []
    
    current_element = numbers[0]
    current_count = 1
    
    for number in numbers[1:]:
        if number == current_element:
            current_count += 1
        else:
            unique_elements.append(current_element)
            counts.append(current_count)
            current_element = number
            current_count = 1
    
    # Append the last element and its count
    unique_elements.append(current_element)
    counts.append(current_count)
    
    return unique_elements, counts

# Test the function with the provided assertion
assert count_duplic([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]) == ([1, 2, 4, 5], [1, 3, 3, 4])
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_duplic([1,2,2,2,4,4,4,5,5,5,5])==([1, 2, 4, 5], [1, 3, 3, 4])
    assert count_duplic([2,2,3,1,2,6,7,9])==([2, 3, 1, 2, 6, 7, 9], [2, 1, 1, 1, 1, 1, 1])
    assert count_duplic([2,1,5,6,8,3,4,9,10,11,8,12])==([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
