# MBPP/859
### Completion
def sub_lists(input_list):
    result = []
    n = len(input_list)
    
    # Generate all possible combinations of the list
    for i in range(1 << n):  # 2^n combinations
        sublist = []
        for j in range(n):
            if i & (1 << j):  # Check if jth element is included
                sublist.append(input_list[j])
        result.append(sublist)
    
    return result

# Test the function with the provided assertion
assert sub_lists([10, 20, 30, 40]) == [[], [10], [20], [30], [40], 
                                        [10, 20], [10, 30], [10, 40], 
                                        [20, 30], [20, 40], [30, 40], 
                                        [10, 20, 30], [10, 20, 40], 
                                        [10, 30, 40], [20, 30, 40], 
                                        [10, 20, 30, 40]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sub_lists([10, 20, 30, 40])==[[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], [10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]
    assert sub_lists(['X', 'Y', 'Z'])==[[], ['X'], ['Y'], ['Z'], ['X', 'Y'], ['X', 'Z'], ['Y', 'Z'], ['X', 'Y', 'Z']]
    assert sub_lists([1,2,3])==[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
