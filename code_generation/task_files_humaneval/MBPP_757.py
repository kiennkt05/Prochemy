# MBPP/757
### Completion
def count_reverse_pairs(string_list):
    # Set to keep track of seen strings
    seen = set()
    # Set to keep track of counted pairs
    counted_pairs = set()
    # Counter for reverse pairs
    reverse_pair_count = 0
    
    for string in string_list:
        # Create the reverse of the current string
        reversed_string = string[::-1]
        
        # Check if the reversed string is in the seen set
        if reversed_string in seen:
            # Create a sorted tuple to represent the pair uniquely
            pair = tuple(sorted((string, reversed_string)))
            # If this pair hasn't been counted yet, count it
            if pair not in counted_pairs:
                counted_pairs.add(pair)
                reverse_pair_count += 1
        
        # Add the current string to the seen set
        seen.add(string)
    
    return str(reverse_pair_count)

# Test case
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
