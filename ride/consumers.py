import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RideTrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.ride_id = self.scope['url_route']['kwargs']['ride_id']
        self.ride_group_name = f"ride_{self.ride_id}"

        await self.channel_layer.group_add(self.ride_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.ride_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        latitude = data['latitude']
        longitude = data['longitude']

        await self.channel_layer.group_send(
            self.ride_group_name,
            {
                'type': 'send_location_update',
                'latitude': latitude,
                'longitude': longitude
            }
        )

    async def send_location_update(self, event):
        latitude = event['latitude']
        longitude = event['longitude']

        # Send location update to WebSocket
        await self.send(text_data=json.dumps({
            'latitude': latitude,
            'longitude': longitude
        }))
