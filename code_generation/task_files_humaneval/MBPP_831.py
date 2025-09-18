# MBPP/831
### Completion
def count_Pairs(array, n):
    # Dictionary to count occurrences of each element
    count_dict = {}
    
    # Count occurrences of each element in the array
    for num in array:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Initialize the total pairs count
    total_pairs = 0
    
    # Calculate pairs for each unique element
    for count in count_dict.values():
        if count > 1:
            total_pairs += count * (count - 1) // 2  # Combination C(n, 2)
    
    return total_pairs

# Test case
assert count_Pairs([1, 1, 1, 1], 4) == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Pairs([1,1,1,1],4) == 6
    assert count_Pairs([1,5,1],3) == 1
    assert count_Pairs([3,2,1,7,8,9],6) == 0
