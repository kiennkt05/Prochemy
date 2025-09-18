# MBPP/636
### Completion
def Check_Solution(a, b, c):
    # Check if the product of the roots equals 1
    if c == a:
        return "Yes"
    else:
        return "No"

# Test the function with the provided assertion
assert Check_Solution(2, 0, 2) == "Yes"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Check_Solution(2,0,2) == "Yes"
    assert Check_Solution(2,-5,2) == "Yes"
    assert Check_Solution(1,2,3) == "No"
