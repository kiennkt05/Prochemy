# MBPP/688
### Completion
import math

def len_complex(real, imag):
    return math.sqrt(real**2 + imag**2)

# Test the function with the provided assertion
assert len_complex(3, 4) == 5.0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert len_complex(3,4)==5.0
    assert len_complex(9,10)==13.45362404707371
    assert len_complex(7,9)==11.40175425099138
