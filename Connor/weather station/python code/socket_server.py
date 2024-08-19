import asyncio
import websockets
import datetime


rain_y_cords = [f"0" for _ in range(480)]
temp_y_cords = [f"0" for _ in range(480)]
seconds_in_day = 24 * 60 * 60  # Total seconds in a day
current_rain = 0
current_temp = 0
getting_data = False
piece_of_data = 1

async def check_date_change():
    global rain_y_cords
    global temp_y_cords
    current_date = datetime.datetime.now().date()  # Get the current date
    while True:
        await asyncio.sleep(60)  # Wait for 60 seconds before checking again
        new_date = datetime.datetime.now().date()
        if new_date != current_date:
            current_date = new_date
            tasks = [client.send("r") for client in connected_clients]
            rain_y_cords = None
            temp_y_cords = None
            rain_y_cords = [f"0" for _ in range(480)]
            temp_y_cords = [f"0" for _ in range(480)]
            await asyncio.gather(*tasks)

async def set_y_cords(y_cords, current_value):
    # Calculate the elapsed time since the start of the day
    now = datetime.datetime.now()
    elapsed_time = (now.hour * 3600) + (now.minute * 60) + now.second
    
    # Determine the starting index
    index = int(round(((elapsed_time / seconds_in_day) * 480)))
    if index >= len(y_cords):
        index = len(y_cords)
    
    # Set items from the starting index
    y_cords[index] = current_value

async def set_rain_y_cords():
    global current_rain
    global rain_y_cords
    await set_y_cords(rain_y_cords, current_rain)

async def set_temp_y_cords():
    global current_temp
    global temp_y_cords
    await set_y_cords(temp_y_cords, current_temp)

# A set to keep track of connected clients
connected_clients = set()
busy_clients = set()

async def echo(websocket, path):
    global current_rain
    global rain_y_cords
    global temp_y_cords
    global current_temp
    global getting_data
    global connected_clients
    global piece_of_data
    # Register the new client
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            global piece_of_data
            print(f"Received: {message}")
            if message == "start":
                piece_of_data = 1
                getting_data = True
            elif getting_data:
                try:
                    if piece_of_data == 2:
                        current_temp = float(message)
                        await set_temp_y_cords()
                    if piece_of_data == 6:
                        current_rain = float(message)
                        await set_rain_y_cords()
                except ValueError:
                    print("Error")
                piece_of_data += 1
            elif message == "end" or piece_of_data == 9:
                getting_data = False
            try:
                if message == "rain_y_cords":
                    print(rain_y_cords)
                    busy_clients.add(websocket)
                    for item in rain_y_cords:
                        await websocket.send(str(item))
                elif message == "temp_y_cords":
                    print(temp_y_cords)
                    for item in temp_y_cords:
                        await websocket.send(str(item))
                    busy_clients.remove(websocket)
            except ValueError:
                print("Error")
            else:
                for client in connected_clients:
                    if not client in busy_clients:
                        await client.send(message)
    except websockets.ConnectionClosed:
        print("Connection was closed.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Unregister the client
        connected_clients.remove(websocket)
async def server():
    # Define the paths to your SSL certificate and key files
    # Start the WebSocket server with SSL/TLS
    start_server = await websockets.serve(echo, "0.0.0.0", 8765)
    print("Server started with SSL...")
    await start_server.wait_closed()

async def main():
    # Run both distribute_items and other_task concurrently
    await asyncio.gather(set_rain_y_cords(), set_temp_y_cords(), server(), check_date_change())

# Start the asyncio event loop
asyncio.run(main())
