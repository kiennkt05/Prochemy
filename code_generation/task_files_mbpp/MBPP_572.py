# MBPP/572
### Completion
def two_unique_nums(lst):
    # Create a dictionary to count occurrences of each number
    count = {}
    
    # Count occurrences of each number in the list
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Collect numbers that appear only once
    unique_nums = [num for num, cnt in count.items() if cnt == 1]
    
    return unique_nums

# Test the function with the provided assertion
assert two_unique_nums([1, 2, 3, 2, 3, 4, 5]) == [1, 4, 5]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
    assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
    assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]
