from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .utils import generate_random_location
import time

def broadcast_fake_location_updates(ride_id, start_lat, start_lon, end_lat, end_lon):
    channel_layer = get_channel_layer()
    coordinates = generate_random_location(start_lat, start_lon, end_lat, end_lon)

    for lat, lon in coordinates:
        async_to_sync(channel_layer.group_send)(
            f"ride_{ride_id}",
            {
                "type": "send_location_update",
                "latitude": lat,
                "longitude": lon,
            }
        )
        time.sleep(1)
