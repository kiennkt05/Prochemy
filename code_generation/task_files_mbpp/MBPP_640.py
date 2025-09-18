# MBPP/640
### Completion
def remove_parenthesis(strings):
    # Initialize an empty list to hold the results
    result = []
    
    for s in strings:
        # Remove the text within parentheses using str.split and str.join
        cleaned_string = ''.join(s.split('(')[0:1])  # Get the part before the first '('
        result.append(cleaned_string.strip())  # Strip any leading/trailing whitespace
    
    return result[0] if result else ""

# Test the function
assert remove_parenthesis(["python (chrome)"]) == "python"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")
