# MBPP/220
### Completion
def replace_max_specialchar(text, n):
    # Define the characters to be replaced
    special_chars = [' ', ',', '.']
    
    # Initialize a counter for replacements
    count = 0
    
    # Create a list to hold the modified characters
    result = []
    
    for char in text:
        if char in special_chars and count < n:
            result.append(':')  # Replace with colon
            count += 1
        else:
            result.append(char)  # Keep the original character
    
    # Join the list into a string and return
    return ''.join(result)

# Test the function with the provided assertion
assert replace_max_specialchar('Python language, Programming language.', 2) == 'Python:language: Programming language.'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_max_specialchar('Python language, Programming language.',2)==('Python:language: Programming language.')
    assert replace_max_specialchar('a b c,d e f',3)==('a:b:c:d e f')
    assert replace_max_specialchar('ram reshma,ram rahim',1)==('ram:reshma,ram rahim')
