# MBPP/117
### Completion
def list_to_float(input_list):
    # Convert each element in the tuples to float if possible
    converted_list = []
    for tup in input_list:
        converted_tup = tuple(float(x) if isinstance(x, str) and x.replace('.', '', 1).isdigit() else x for x in tup)
        converted_list.append(converted_tup)
    
    return str(converted_list)

# Test the function with the provided assertion
assert list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]) == '[(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert list_to_float( [("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")] ) == '[(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]'
    assert list_to_float( [("4", "4"), ("2", "27"), ("4.12", "9"), ("7", "11")] ) == '[(4.0, 4.0), (2.0, 27.0), (4.12, 9.0), (7.0, 11.0)]'
    assert list_to_float( [("6", "78"), ("5", "26.45"), ("1.33", "4"), ("82", "13")] ) == '[(6.0, 78.0), (5.0, 26.45), (1.33, 4.0), (82.0, 13.0)]'
