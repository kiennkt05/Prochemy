# MBPP/880
### Completion
def Check_Solution(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Determine the number of solutions based on the discriminant
    if D > 0:
        return "2 solutions"
    elif D == 0:
        return "1 solution"
    else:
        return "0 solutions"

# Example assertion
assert Check_Solution(2, 5, 2) == "2 solutions"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Check_Solution(2,5,2) == "2 solutions"
    assert Check_Solution(1,1,1) == "No solutions"
    assert Check_Solution(1,2,1) == "1 solution"
