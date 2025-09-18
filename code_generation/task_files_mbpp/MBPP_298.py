# MBPP/298
### Completion
def intersection_nested_lists(main_list, nested_list):
    # Create a new nested list to hold the results
    result = []
    
    # Iterate through each sublist in the nested list
    for sublist in nested_list:
        # Find the intersection of the sublist with the main list
        intersection = [item for item in sublist if item in main_list]
        # Append the intersection to the result
        result.append(intersection)
    
    return result

# Test the function with the provided assertion
assert intersection_nested_lists(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
) == [[12], [7, 11], [1, 5, 8]]

print("Function works correctly!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert intersection_nested_lists( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==[[12], [7, 11], [1, 5, 8]]
    assert intersection_nested_lists([[2, 3, 1], [4, 5], [6, 8]], [[4, 5], [6, 8]])==[[], []]
    assert intersection_nested_lists(['john','amal','joel','george'],[['john'],['jack','john','mary'],['howard','john'],['jude']])==[['john'], ['john'], ['john'], []]
