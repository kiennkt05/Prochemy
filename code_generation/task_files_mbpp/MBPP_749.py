# MBPP/749
### Completion
def sort_numeric_strings(string_list):
    # Convert the list of strings to a list of integers
    num_list = [int(num) for num in string_list]
    # Sort the list of integers
    num_list.sort()
    return num_list

# Test the function with the provided assertion
assert sort_numeric_strings(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']) == [-500, -12, 0, 4, 7, 12, 45, 100, 200]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
    assert sort_numeric_strings(['2','3','8','4','7','9','8','2','6','5','1','6','1','2','3','4','6','9','1','2'])==[1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9, 9]
    assert sort_numeric_strings(['1','3','5','7','1', '3','13', '15', '17','5', '7 ','9','1', '11'])==[1, 1, 1, 3, 3, 5, 5, 7, 7, 9, 11, 13, 15, 17]
