# MBPP/175
### Completion
def is_valid_parenthese(s: str) -> bool:
    stack = []
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map.keys():  # If it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # Pop the last opening bracket from the stack
    
    return len(stack) == 0  # If stack is empty, all brackets are valid

# Test the function
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
