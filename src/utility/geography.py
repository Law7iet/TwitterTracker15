import math
import requests
from urllib.parse import urlencode

# Calcola approssimativamente il centro di un quadrato
# Il quadrato e' descritto mediante 4 coordinate che rappresentano i suoi vertici
# Le coordinate sono una coppia di valori rappresentati da una lista con 2 elementi
# INPUT: una lista di coordinate in stringhe
# OUTPUT: le coordinate rappresentati da una lista di float
def coordinate_calculator(coordinates):
    bottom_left = coordinates[0]
    bottom_right = coordinates[1]
    top_right = coordinates[2]
    top_left = coordinates[3]
    if bottom_left == bottom_right == top_right == top_left:
        # I 4 vertici sono uguali
        return [float(bottom_left[0]), float(bottom_left[1])]
    else:
        # I 4 vertici non sono uguali
        longitude = (float(bottom_left[0]) + float(bottom_right[0])) / 2
        latitude = (float(bottom_right[1]) + float(top_right[1])) / 2
        return [longitude, latitude]

# Converte approssimativamente le coordinate da gradi centigradi in chilometri
# INPUT: le coordinate in gradi centigradi rappresentati da una lista di float
# OUTPUT: le coordinate in chilometri rappresentati da una lista di float
def convert_coordinates_to_km(coordinates):
    latitude = coordinates[1] * 110.574
    longitude = coordinates[0] * 111.320 * (math.cos(math.radians(coordinates[1])))
    return [longitude, latitude]

# Converte approssimativamente le coordinate da gradi centigradi in chilometri
# INPUT: le coordinate in chilometri rappresentati da una lista di float
# OUTPUT: le coordinate in gradi centigradi rappresentati da una lista di float
def convert_coordinates_to_degrees(coordinates):
    latitude = coordinates[1] / 110.574
    longitude = coordinates[0] / (111.320 * (math.cos(math.radians(latitude))))
    return [longitude, latitude]

# Controlla se un luogo e' all'interno di un'area
# INPUT: il centro dell'area, una lista di 2 stringhe
# INPUT: il semilato dell'area quadrata in stringa
# INPUT: il luogo, una lista di 4 coordinate
def is_in(coordinates, radius, place):
    # Inizializzazione dei dati
    coordinates = [float(coordinates[0]), float(coordinates[1])]
    radius = radius[0 : -2]
    radius = float(radius)
    coordinates_km = convert_coordinates_to_km(coordinates)
    # Calcolo della coordinata in alto a sinistra dell'area
    y = coordinates_km[0] + radius
    x = coordinates_km[1] - radius
    bottom_right = convert_coordinates_to_degrees([y, x])
    # Calcolo della coordinata in basso a destra dell'area
    y = coordinates_km[0] - radius
    x = coordinates_km[1] + radius
    top_left = convert_coordinates_to_degrees([y, x])
    # Calcolo del centro del luogo
    place = coordinate_calculator(place)
    # Controllo se il luogo e' all'interno dell'area
    if place[0] >= top_left[0] and place[0] <= bottom_right[0]:
        if place[1] >= bottom_right[1] and place[1] <= top_left[1]:
            return True
    return False

# Cerca le coordinate di un luogo
# Il luogo è dato dalla stringa
# INPUT: una stringa
# OUTPUT: una lista composta da due valori
def convert_address_to_coordinates(indirizzo):
    api_key = 'AIzaSyAR2Ha_6_KY2827W7UzJ2s3Y7tj6d4f0QI'
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': indirizzo, 'key': api_key}
    url_params = urlencode(params)
    url = endpoint + '?' + url_params
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return -2
    else:
        try:
            coordinate = r.json()['results'][0]['geometry']['location']
            return [coordinate['lng'], coordinate['lat']]
        except:
            return -1

# Converte il luogo in input in un indirizzo completo
# INPUT: una stringa
# OUTPUT: una stringa
def get_address(indirizzo):
    api_key = 'AIzaSyAR2Ha_6_KY2827W7UzJ2s3Y7tj6d4f0QI'
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': indirizzo, 'key': api_key}
    url_params = urlencode(params)
    url = endpoint + '?' + url_params
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return -2
    else:
        try:
            x = (r.json()['results'][0]['address_components'])
            indirizzo = ''
            for i in x:
                indirizzo += (i['long_name'] + ', ')
            indirizzo = indirizzo[:-1]
            return indirizzo
        except:
            return -1
