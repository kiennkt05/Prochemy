# MBPP/131
### Completion
def reverse_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    s_list = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s_list[left] in vowels and s_list[right] in vowels:
            # Swap the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        if s_list[left] not in vowels:
            left += 1
        if s_list[right] not in vowels:
            right -= 1

    return ''.join(s_list)

# Test the function with the provided assertion
assert reverse_vowels("Python") == "Python"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("ab") == "ab"
