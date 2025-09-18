# MBPP/640
### Completion
import re

def remove_parenthesis(strings):
    """
    Remove the parenthesis area from each string in the input list.

    Args:
    strings (list of str): A list of strings from which to remove parenthesis.

    Returns:
    list of str: A new list of strings with parenthesis and their contents removed.
    """
    # Use a regular expression to remove text within parentheses
    cleaned_strings = [re.sub(r'\s*\(.*?\)\s*', ' ', s).strip() for s in strings]
    return cleaned_strings

# Test the function with the provided test case
assert remove_parenthesis(["python (chrome)"]) == ["python"]

# Additional test cases
assert remove_parenthesis(["hello (world)", "test (example) string"]) == ["hello", "test string"]
assert remove_parenthesis(["no parentheses here"]) == ["no parentheses here"]
assert remove_parenthesis(["(remove this) keep this"]) == ["keep this"]
assert remove_parenthesis(["(a) (b) (c)"]) == [""]

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_parenthesis(["python (chrome)"])==("python")
    assert remove_parenthesis(["string(.abc)"])==("string")
    assert remove_parenthesis(["alpha(num)"])==("alpha")
