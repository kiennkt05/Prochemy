# MBPP/323
### Completion
def re_arrange(arr, n):
    # Separate positive and negative numbers
    positive = [x for x in arr if x >= 0]
    negative = [x for x in arr if x < 0]
    
    # Initialize the result array
    result = []
    
    # Use two pointers to merge the two lists
    pos_index, neg_index = 0, 0
    while pos_index < len(positive) and neg_index < len(negative):
        # Append one negative and one positive alternatively
        result.append(negative[neg_index])
        result.append(positive[pos_index])
        neg_index += 1
        pos_index += 1
    
    # If there are remaining positive numbers, append them
    while pos_index < len(positive):
        result.append(positive[pos_index])
        pos_index += 1
    
    # If there are remaining negative numbers, append them
    while neg_index < len(negative):
        result.append(negative[neg_index])
        neg_index += 1
    
    return result

# Test case
assert re_arrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8], 10) == [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert re_arrange([-5, -2, 5, 2, 4,	7, 1, 8, 0, -8], 10) == [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
    assert re_arrange([1, 2, 3, -4, -1, 4], 6) == [-4, 1, -1, 2, 3, 4]
    assert re_arrange([4, 7, 9, 77, -4, 5, -3, -9], 8) == [-4, 4, -3, 7, -9, 9, 77, 5]
