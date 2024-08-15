import asyncio
import websockets

async def test_connection():
    uri = "ws://localhost:8765/"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        response = await websocket.recv()
        print(f"Received response: {response}")

asyncio.run(test_connection())
