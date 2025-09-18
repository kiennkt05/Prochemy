# MBPP/864
### Completion
def palindrome_lambda(strings):
    # Lambda function to check if a string is a palindrome
    is_palindrome = lambda s: s == s[::-1]
    
    # Use filter to apply the lambda function and return a list of palindromes
    return list(filter(is_palindrome, strings))

# Test case
assert palindrome_lambda(["php", "res", "Python", "abcd", "Java", "aaa"]) == ['php', 'aaa']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert palindrome_lambda(["php", "res", "Python", "abcd", "Java", "aaa"])==['php', 'aaa']
    assert palindrome_lambda(["abcd", "Python", "abba", "aba"])==['abba', 'aba']
    assert palindrome_lambda(["abcd", "abbccbba", "abba", "aba"])==['abbccbba', 'abba', 'aba']
