# MBPP/805
### Completion
def max_sum_list(lists):
    # Initialize variables to track the maximum sum and the corresponding list
    max_sum = float('-inf')
    max_list = []

    # Iterate through each list in the list of lists
    for lst in lists:
        current_sum = sum(lst)  # Calculate the sum of the current list
        # Update max_sum and max_list if the current sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = lst

    return max_list

# Test the function with the provided assertion
assert max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12] 
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10] 
    assert max_sum_list([[2,3,1]])==[2,3,1] 
