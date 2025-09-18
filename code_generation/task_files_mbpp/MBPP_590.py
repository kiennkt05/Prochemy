# MBPP/590
### Completion
import math

def polar_rect(r, theta):
    # Calculate rectangular coordinates
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    # Return the rectangular coordinates as a tuple and as a complex number
    return (x, y), complex(x, y)

# Test the function with the provided assertion
assert polar_rect(3, 4) == ((-3.0, -0.0), (-3+0j))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    assert polar_rect(4,7)==((8.06225774829855, 1.0516502125483738), (-2+2.4492935982947064e-16j))
    assert polar_rect(15,17)==((22.67156809750927, 0.8478169733934057), (-2+2.4492935982947064e-16j))
