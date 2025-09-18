# MBPP/374
### Completion
def permute_string(s):
    # Helper function to generate permutations
    def generate_permutations(current, remaining):
        if len(remaining) == 0:
            results.append(current)
        else:
            for i in range(len(remaining)):
                # Fix the character at index i and generate permutations of the rest
                next_current = current + remaining[i]
                next_remaining = remaining[:i] + remaining[i+1:]
                generate_permutations(next_current, next_remaining)

    results = []
    generate_permutations("", s)
    return results

# Test case
assert permute_string('ab') == ['ab', 'ba']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert permute_string('ab')==['ab', 'ba']
    assert permute_string('abc')==['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    assert permute_string('abcd')==['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
