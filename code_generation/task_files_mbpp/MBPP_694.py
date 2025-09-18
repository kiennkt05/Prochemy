# MBPP/694
### Completion
def extract_unique(input_dict):
    unique_values = set()  # Use a set to store unique values
    for value_list in input_dict.values():
        unique_values.update(value_list)  # Add values to the set
    return sorted(unique_values)  # Return a sorted list of unique values

# Test the function with the provided assertion
assert extract_unique({'msm': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}) == [1, 2, 5, 6, 7, 8, 10, 11, 12]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_unique({'msm' : [5, 6, 7, 8],'is' : [10, 11, 7, 5],'best' : [6, 12, 10, 8],'for' : [1, 2, 5]} ) == [1, 2, 5, 6, 7, 8, 10, 11, 12]
    assert extract_unique({'Built' : [7, 1, 9, 4],'for' : [11, 21, 36, 14, 9],'ISP' : [4, 1, 21, 39, 47],'TV' : [1, 32, 38]} ) == [1, 4, 7, 9, 11, 14, 21, 32, 36, 38, 39, 47]
    assert extract_unique({'F' : [11, 13, 14, 17],'A' : [12, 11, 15, 18],'N' : [19, 21, 15, 36],'G' : [37, 36, 35]}) == [11, 12, 13, 14, 15, 17, 18, 19, 21, 35, 36, 37]
