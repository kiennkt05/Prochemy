# MBPP/859
### Completion
def sub_lists(input_list):
    """
    Generate all possible sublists of the given list.

    Parameters:
    input_list (list): The list from which to generate sublists.

    Returns:
    list: A list containing all sublists of the input list.
    """
    result = []
    n = len(input_list)
    
    # There are 2^n possible combinations (including the empty list)
    for i in range(1 << n):  # This is equivalent to 2**n
        sublist = []
        for j in range(n):
            # Check if the j-th element is included in the current combination
            if i & (1 << j):
                sublist.append(input_list[j])
        result.append(sublist)
    
    return result

# Test case
assert sub_lists([10, 20, 30, 40]) == [
    [], 
    [10], 
    [20], 
    [30], 
    [40], 
    [10, 20], 
    [10, 30], 
    [10, 40], 
    [20, 30], 
    [20, 40], 
    [30, 40], 
    [10, 20, 30], 
    [10, 20, 40], 
    [10, 30, 40], 
    [20, 30, 40], 
    [10, 20, 30, 40]
]

print("All sublists generated successfully.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sub_lists([10, 20, 30, 40])==[[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], [10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]
    assert sub_lists(['X', 'Y', 'Z'])==[[], ['X'], ['Y'], ['Z'], ['X', 'Y'], ['X', 'Z'], ['Y', 'Z'], ['X', 'Y', 'Z']]
    assert sub_lists([1,2,3])==[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
