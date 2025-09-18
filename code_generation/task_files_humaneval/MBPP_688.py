# MBPP/688
### Completion
import math

def len_complex(real, imag):
    """
    Calculate the length (magnitude) of a complex number.

    Parameters:
    real (float): The real part of the complex number.
    imag (float): The imaginary part of the complex number.

    Returns:
    float: The length of the complex number.
    """
    return math.sqrt(real**2 + imag**2)

# Test case
assert len_complex(3, 4) == 5.0, "Test case failed!"
print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert len_complex(3,4)==5.0
    assert len_complex(9,10)==13.45362404707371
    assert len_complex(7,9)==11.40175425099138
