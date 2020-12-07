'''
Created on 3 dic 2020

@author: L
'''

import math 

# Calculate the center's coordinates of an area
# INPUT: a list of 4 coordinates
# OUTPUT: the center's coordinates (list of float)
def coordinate_calculator(coordinates):
    bottom_left = coordinates[0]
    bottom_right = coordinates[1]
    top_right = coordinates[2]
    top_left = coordinates[3]
    
    if bottom_left == bottom_right == top_right == top_left:
        # it's a place, so the coordinates are the same
        return [float(bottom_left[0]), float(bottom_left[1])]
    else:
        # it's a city, there're 4 different coordinates
        longitude = (float(bottom_left[0]) + float(bottom_right[0])) / 2
        latitude = (float(bottom_right[1]) + float(top_right[1])) / 2
        return [longitude, latitude]
    
# Convert the coordinates from degrees to km
# INPUT: a list rappresents the couple of coordinates in degrees (float)
# OUTPUT: a list rappresents the couple of coordinates in km (float)
def convert_coordinates_to_km(coordinates):
    latitude = coordinates[1] * 110.574 
    longitude = coordinates[0] * 111.320 * (math.cos(math.radians(coordinates[1])))
    return [longitude, latitude]

# Convert the coordinates from km to degrees
# INPUT: a list rappresents the couple of coordinates in km (float)
# OUTPUT: a list rappresents the couple of coordinates in degreesz (float)
def convert_coordinates_to_degrees(coordinates):
    latitude = coordinates[1] / 110.574 
    longitude = coordinates[0] / (111.320 * (math.cos(math.radians(latitude))))
    return [longitude, latitude]

def is_in(coordinates, radius, place):
    
    coordinates = [float(coordinates[0]), float(coordinates[1])]
    radius = radius[0 : -2];
    radius = float(radius)
    
    coordinates_km = convert_coordinates_to_km(coordinates)
    
    # top_left's coordinates
    y = coordinates_km[0] + radius
    x = coordinates_km[1] - radius
    bottom_right = convert_coordinates_to_degrees([y, x])
    
    # top_right's coordinates
    y = coordinates_km[0] + radius
    x = coordinates_km[1] + radius
    top_right = convert_coordinates_to_degrees([y, x])
    
    # bottom_left's coordinates
    y = coordinates_km[0] - radius
    x = coordinates_km[1] - radius
    bottom_left = convert_coordinates_to_degrees([y, x])
    
    # bottom_right's coordinates
    y = coordinates_km[0] - radius
    x = coordinates_km[1] + radius
    top_left = convert_coordinates_to_degrees([y, x])

    place = coordinate_calculator(place)
    
    if place[0] >= top_left[0] and place[0] <= bottom_right[0]:
        if place[1] >= bottom_right[1] and place[1] <= top_left[1]:
            return True
    return False