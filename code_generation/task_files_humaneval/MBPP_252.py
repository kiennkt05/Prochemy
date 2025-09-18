# MBPP/252
### Completion
import cmath

def convert(z):
    """
    Convert a complex number to polar coordinates.

    Parameters:
    z (complex or float): The complex number to convert. Can be a complex number or a real number.

    Returns:
    tuple: A tuple containing the magnitude and angle in radians (r, theta).
    """
    # If z is a real number, convert it to a complex number
    if isinstance(z, (int, float)):
        z = complex(z, 0)
    
    # Calculate the polar coordinates
    r = abs(z)  # Magnitude
    theta = cmath.phase(z)  # Angle in radians
    
    return (r, theta)

# Test case
assert convert(1) == (1.0, 0.0)

# Additional test cases for verification
assert convert(0) == (0.0, 0.0)  # Zero case
assert convert(1 + 1j) == (2**0.5, cmath.pi / 4)  # 1 + 1i
assert convert(-1) == (1.0, cmath.pi)  # Negative real number
assert convert(0 + 1j) == (1.0, cmath.pi / 2)  # Pure imaginary number
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0,0.0)
    assert convert(5) == (5.0,0.0)
