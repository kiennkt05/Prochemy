# MBPP/780
### Completion
def find_combinations(tuple_list):
    # Initialize an empty set to store unique combinations of sums
    result_set = set()
    
    # Get the number of tuples in the list
    n = len(tuple_list)
    
    # Iterate over all unique pairs of tuples
    for i in range(n):
        for j in range(n):
            if i != j:  # Ensure we do not sum the same tuple with itself
                # Calculate the sum of the tuples
                sum_tuple = (tuple_list[i][0] + tuple_list[j][0], tuple_list[i][1] + tuple_list[j][1])
                # Add the sum tuple to the set
                result_set.add(sum_tuple)
    
    # Convert the set to a sorted list before returning
    return sorted(result_set)

# Test the function with the provided test case
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]

# Print the result for verification
print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
    assert find_combinations([(3, 5), (7, 8), (6, 2), (7, 11)]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]
    assert find_combinations([(4, 6), (8, 9), (7, 3), (8, 12)]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]
