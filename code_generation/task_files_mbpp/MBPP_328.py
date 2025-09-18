# MBPP/328
### Completion
def rotate_left(lst, num_rotations, start_index):
    # Adjust the start_index to be within the bounds of the list
    start_index = start_index % len(lst)
    
    # Split the list into two parts: before and after the start_index
    part1 = lst[start_index:]
    part2 = lst[:start_index]
    
    # Rotate the list by combining the two parts and slicing
    rotated_list = part1 + part2
    
    # Rotate the list further by the specified number of rotations
    num_rotations = num_rotations % len(rotated_list)
    rotated_list = rotated_list[num_rotations:] + rotated_list[:num_rotations]
    
    return rotated_list

# Test the function with the provided assertion
assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 4) == [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2)==[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2]
