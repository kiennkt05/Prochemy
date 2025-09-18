# MBPP/180
### Completion
import math

def distance_lat_long(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Haversine formula
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    # Distance in kilometers
    distance = R * c
    return distance

# Test the function with the provided assertion
assert distance_lat_long(23.5, 67.5, 25.5, 69.5) == 12179.372041317429
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert distance_lat_long(23.5,67.5,25.5,69.5)==12179.372041317429
    assert distance_lat_long(10.5,20.5,30.5,40.5)==6069.397933300514
    assert distance_lat_long(10,20,30,40)==6783.751974994595
