# MBPP/638
### Completion
def wind_chill(temperature, wind_speed):
    """
    Calculate the wind chill index based on the temperature and wind speed.
    
    Parameters:
    temperature (float): The air temperature in degrees Fahrenheit.
    wind_speed (float): The wind speed in miles per hour.
    
    Returns:
    float: The wind chill index.
    """
    wci = (35.74 + 
            0.6215 * temperature - 
            35.75 * (wind_speed ** 0.16) + 
            0.4275 * temperature * (wind_speed ** 0.16))
    return wci

# Test the function with the provided assertion
assert wind_chill(120, 35) == 40
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert wind_chill(120,35)==40
    assert wind_chill(40,70)==86
    assert wind_chill(10,100)==116
