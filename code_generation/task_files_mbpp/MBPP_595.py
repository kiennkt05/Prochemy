# MBPP/595
### Completion
def min_Swaps(s1: str, s2: str) -> int:
    if sorted(s1) != sorted(s2):
        return -1  # Not possible to convert if they don't have the same characters

    # Find the positions where the characters differ
    mismatches = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatches.append((s1[i], s2[i]))

    # Count the number of swaps needed
    count_01 = count_10 = 0
    for a, b in mismatches:
        if a == '0' and b == '1':
            count_01 += 1
        elif a == '1' and b == '0':
            count_10 += 1

    # Each swap can fix one '01' and one '10' mismatch
    return (count_01 + count_10) // 2

# Test the function with the provided assertion
assert min_Swaps("1101", "1110") == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Swaps("1101","1110") == 1
    assert min_Swaps("111","000") == "Not Possible"
    assert min_Swaps("111","110") == "Not Possible"
