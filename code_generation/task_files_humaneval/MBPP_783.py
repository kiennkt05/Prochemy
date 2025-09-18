# MBPP/783
### Completion
def rgb_to_hsv(r, g, b):
    # Normalize RGB values to the range [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0
    
    # Find the maximum and minimum values of r, g, b
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    
    # Calculate Value (V)
    v = max_c
    
    # Calculate Saturation (S)
    if max_c == 0:
        s = 0
    else:
        s = (max_c - min_c) / max_c
    
    # Calculate Hue (H)
    if max_c == min_c:
        h = 0  # Undefined hue
    elif max_c == r:
        h = (60 * ((g - b) / (max_c - min_c)) + 360) % 360
    elif max_c == g:
        h = (60 * ((b - r) / (max_c - min_c)) + 120) % 360
    elif max_c == b:
        h = (60 * ((r - g) / (max_c - min_c)) + 240) % 360
    
    # Convert S and V to percentage
    s *= 100
    v *= 100
    
    return (h, s, v)

# Test the function with the provided test case
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)

# Additional test cases for verification
assert rgb_to_hsv(0, 0, 0) == (0, 0.0, 0.0)  # Black
assert rgb_to_hsv(255, 0, 0) == (0, 100.0, 100.0)  # Red
assert rgb_to_hsv(0, 255, 0) == (120, 100.0, 100.0)  # Green
assert rgb_to_hsv(0, 0, 255) == (240, 100.0, 100.0)  # Blue
assert rgb_to_hsv(255, 255, 0) == (60, 100.0, 100.0)  # Yellow
assert rgb_to_hsv(255, 0, 255) == (300, 100.0, 100.0)  # Magenta
assert rgb_to_hsv(0, 255, 255) == (180, 100.0, 100.0)  # Cyan

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)
