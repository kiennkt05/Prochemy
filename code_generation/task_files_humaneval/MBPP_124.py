# MBPP/124
### Completion
import cmath

def angle_complex(z):
    """
    Calculate the angle (argument) of a complex number.

    Parameters:
    z (complex): A complex number.

    Returns:
    float: The angle of the complex number in radians.
    """
    return cmath.phase(z)

# Test case
assert angle_complex(1j) == 1.5707963267948966  # This is the angle for the complex number 0 + 1j
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert angle_complex(0,1j)==1.5707963267948966 
    assert angle_complex(2,1j)==0.4636476090008061
    assert angle_complex(0,2j)==1.5707963267948966
