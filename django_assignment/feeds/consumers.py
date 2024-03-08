
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import websockets

class LiveFeedConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.consumer_group = "live_feed"
        await self.channel_layer.group_add(
            self.consumer_group,self.channel_name
        )
        await self.accept()
        uri = "wss://dstream.binance.com/stream?streams=btcusd_perp@bookTicker"
        async with websockets.connect(uri) as websocket:
            while websocket:
                data = await websocket.recv()
                await self.send(text_data=data)
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("live_feeds", self.channel_name)

    async def receive(self, text_data):
        pass

    async def send_live_feed(self, event):
        live_feed = event['message']
        await self.send(text_data=json.dumps({'message': live_feed}))