# MBPP/175
### Completion
def is_valid_parenthese(s: str) -> bool:
    # Dictionary to hold matching pairs of parentheses
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening parentheses
    stack = []

    # Iterate through each character in the string
    for char in s:
        # If the character is a closing parenthesis
        if char in matching_parentheses:
            # Pop the top element from the stack if it's not empty, else assign a dummy value
            top_element = stack.pop() if stack else None
            
            # Check if the popped element matches the corresponding opening parenthesis
            if matching_parentheses[char] != top_element:
                return False
        else:
            # If it's an opening parenthesis, push it onto the stack
            stack.append(char)

    # If the stack is empty, all parentheses were matched; otherwise, it's invalid
    return len(stack) == 0

# Test case
assert is_valid_parenthese("(){}[]") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_valid_parenthese("(){}[]")==True
    assert is_valid_parenthese("()[{)}")==False
    assert is_valid_parenthese("()")==True
