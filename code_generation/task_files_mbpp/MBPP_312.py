# MBPP/312
### Completion
import math

def volume_cone(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

# Test the function with the provided assertion
assert volume_cone(5, 12) == 314.15926535897927
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert volume_cone(5,12)==314.15926535897927
    assert volume_cone(10,15)==1570.7963267948965
    assert volume_cone(19,17)==6426.651371693521
