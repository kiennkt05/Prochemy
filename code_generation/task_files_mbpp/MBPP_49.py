# MBPP/49
### Completion
def specified_element(two_d_list, index):
    return [row[index] for row in two_d_list]

# Example usage
result = specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 0)
print(result)  # Output: [1, 4, 7]

# Assertion to verify the function works as expected
assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 0) == [1, 4, 7]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],0)==[1, 4, 7]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],2)==[3, 6, 9]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]],1)==[2,5,1]
