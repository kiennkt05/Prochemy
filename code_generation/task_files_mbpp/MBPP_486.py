# MBPP/486
### Completion
import math

def binomial_probability(n, k, p):
    # Calculate the binomial coefficient
    binomial_coefficient = math.comb(n, k)
    # Calculate the probability
    probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
    return probability

# Test the function with the provided assertion
assert binomial_probability(10, 5, 1.0/3) == 0.13656454808718185
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binomial_probability(10, 5, 1.0/3) == 0.13656454808718185
    assert binomial_probability(11, 6, 2.0/4) == 0.2255859375
    assert binomial_probability(12, 7, 3.0/5) == 0.227030335488
