# MBPP/864
### Completion
def palindrome_lambda(strings):
    return list(filter(lambda s: s == s[::-1], strings))

# Test the function with the provided assertion
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
