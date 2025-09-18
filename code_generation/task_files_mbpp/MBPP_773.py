# MBPP/773
### Completion
def occurance_substring(main_string, substring):
    start_index = main_string.find(substring)
    if start_index != -1:
        end_index = start_index + len(substring)
        return (substring, start_index, end_index)
    return None  # Return None if the substring is not found

# Test the function with the provided assertion
assert occurance_substring('python programming, python language', 'python') == ('python', 0, 6)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
