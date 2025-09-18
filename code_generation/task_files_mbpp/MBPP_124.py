# MBPP/124
### Completion
import cmath

def angle_complex(z):
    return cmath.phase(z)

# Test the function with the provided assertion
assert angle_complex(1j) == 1.5707963267948966
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert angle_complex(0,1j)==1.5707963267948966 
    assert angle_complex(2,1j)==0.4636476090008061
    assert angle_complex(0,2j)==1.5707963267948966
