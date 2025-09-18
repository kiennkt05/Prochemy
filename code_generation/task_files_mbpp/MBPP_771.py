# MBPP/771
### Completion
def check_expression(expression):
    # Dictionary to hold matching pairs of brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []

    for char in expression:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the topmost element from the stack if it's not empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped bracket matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        # If it's an opening bracket, push onto the stack
        else:
            stack.append(char)

    # If the stack is empty, all brackets were matched; otherwise, it's unbalanced
    return not stack

# Test the function with the provided assertion
assert check_expression("{()}[{}]") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True
