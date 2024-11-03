import random

def generate_random_location(start_lat, start_lon, end_lat, end_lon, steps=20):
    lat_diff = (end_lat - start_lat) / steps
    lon_diff = (end_lon - start_lon) / steps
    coordinates = []

    for i in range(steps):
        lat = start_lat + lat_diff * i + random.uniform(-0.0005, 0.0005)
        lon = start_lon + lon_diff * i + random.uniform(-0.0005, 0.0005)
        coordinates.append((lat, lon))

    return coordinates
