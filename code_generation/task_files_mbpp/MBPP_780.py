# MBPP/780
### Completion
def find_combinations(tuple_list):
    result = []
    n = len(tuple_list)
    
    for i in range(n):
        for j in range(n):
            if i != j:  # Ensure we are not adding the same tuple
                sum_tuple = (tuple_list[i][0] + tuple_list[j][0], tuple_list[i][1] + tuple_list[j][1])
                result.append(sum_tuple)
    
    # Remove duplicates by converting to a set and back to a list
    result = list(set(result))
    
    return result

# Test the function with the provided assertion
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
    assert find_combinations([(3, 5), (7, 8), (6, 2), (7, 11)]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]
    assert find_combinations([(4, 6), (8, 9), (7, 3), (8, 12)]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]
