# MBPP/323
### Completion
def re_arrange(arr, n):
    # Separate positive and negative numbers
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    
    # Initialize the result array
    result = [0] * n
    
    # Pointers for positive and negative numbers
    pos_index = 0
    neg_index = 0
    
    # Fill the result array with alternating positive and negative numbers
    for i in range(n):
        if i % 2 == 0:  # Even index - place positive number
            if pos_index < len(pos):
                result[i] = pos[pos_index]
                pos_index += 1
            else:
                # If no positive numbers left, fill with negative
                result[i] = neg[neg_index]
                neg_index += 1
        else:  # Odd index - place negative number
            if neg_index < len(neg):
                result[i] = neg[neg_index]
                neg_index += 1
            else:
                # If no negative numbers left, fill with positive
                result[i] = pos[pos_index]
                pos_index += 1
    
    return result

# Test the function with the provided assertion
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
