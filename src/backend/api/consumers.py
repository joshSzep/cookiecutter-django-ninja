import asyncio
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timezone import now


class TimeConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        """Handle WebSocket connection."""
        await self.accept()
        self.running = True
        asyncio.create_task(self.send_time())

    async def disconnect(self, code: int | None = None) -> None:
        """Handle WebSocket disconnection."""
        self.running = False

    async def receive(
        self, text_data: str | None = None, bytes_data: bytes | None = None
    ) -> None:
        """Handle incoming WebSocket messages."""
        pass

    async def send_time(self) -> None:
        """Send current time to the client every second."""
        while self.running:
            current_time = now().strftime("%Y-%m-%d %H:%M:%S")
            await self.send(
                text_data=json.dumps(
                    {
                        "type": "time.update",
                        "time": current_time,
                    }
                )
            )
            await asyncio.sleep(1)
