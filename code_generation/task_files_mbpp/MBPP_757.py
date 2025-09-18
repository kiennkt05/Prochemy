# MBPP/757
### Completion
def count_reverse_pairs(string_list):
    # Create a set to store the unique strings for quick lookup
    string_set = set(string_list)
    count = 0
    
    # Iterate through the list of strings
    for string in string_list:
        # Check if the reverse of the string is in the set
        reversed_string = string[::-1]
        if reversed_string in string_set:
            count += 1
            
            # Remove the reversed string from the set to avoid double counting
            string_set.remove(reversed_string)
    
    # Since each pair is counted twice, we divide the count by 2
    return str(count // 2)

# Test the function with the provided assertion
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]) == '2'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== '2'
    assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == '1'
    assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == '2' 
