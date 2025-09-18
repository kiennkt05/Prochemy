# MBPP/91
### Completion
def find_substring(string_list, substring):
    for string in string_list:
        if substring in string:
            return True
    return False

# Test the function with the provided assertion
assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True
