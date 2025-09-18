# MBPP/783
### Completion
def rgb_to_hsv(r, g, b):
    # Normalize the RGB values to the range [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Find the maximum and minimum values of r, g, b
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn

    # Calculate the hue
    if df == 0:
        h = 0  # Achromatic
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    else:  # mx == b
        h = (60 * ((r - g) / df) + 240) % 360

    # Calculate the saturation
    s = 0 if mx == 0 else (df / mx)

    # Calculate the value
    v = mx

    # Convert to percentage
    s *= 100
    v *= 100

    return (h, s, v)

# Test the function with the provided assertion
assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
    assert rgb_to_hsv(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)
