# MBPP/181
### Completion
def common_prefix(strings, length):
    if not strings:
        return ""
    
    # Find the shortest string in the list
    shortest_string = min(strings, key=len)
    
    # Initialize the common prefix
    common_prefix = ""
    
    # Iterate through the characters of the shortest string
    for i in range(length):
        # Check if we are within the bounds of the shortest string
        if i < len(shortest_string):
            # Get the current character from the first string
            current_char = shortest_string[i]
            # Check if this character is the same in all strings
            for string in strings:
                if string[i] != current_char:
                    return common_prefix
            # If all strings have the same character at this position, add it to the prefix
            common_prefix += current_char
        else:
            break
    
    return common_prefix

# Test case
assert common_prefix(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert common_prefix(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'
    assert common_prefix(["apples", "ape", "april"], 3) == 'ap'
    assert common_prefix(["teens", "teenager", "teenmar"], 3) == 'teen'
