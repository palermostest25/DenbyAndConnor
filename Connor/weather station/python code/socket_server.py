import asyncio
import websockets
import datetime

# List of 480 items
rain_y_cords = [f"0" for _ in range(480)]
temp_y_cords = [f"0" for _ in range(480)]
seconds_in_day = 24 * 60 * 60  # Total seconds in a day
interval = seconds_in_day / len(rain_y_cords)  # Interval between setting each item
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
    global interval
    start_time = datetime.datetime.now()
    # Calculate the elapsed time since the start of the day
    now = datetime.datetime.now()
    start_of_day = datetime.datetime.combine(now.date(), datetime.time.min)
    elapsed_time = (now - start_of_day).total_seconds()
    
    # Determine the starting index
    start_index = int(elapsed_time // interval)
    if start_index >= len(y_cords):
        start_index = len(y_cords) - 1
    
    # Set items from the starting index
    for i in range(start_index, start_index + 1, len(y_cords)):
        # Calculate when to set the next item
        target_time = start_time + datetime.timedelta(seconds=(i - start_index) * interval)
        time_to_wait = (target_time - datetime.datetime.now()).total_seconds()
        if time_to_wait > 0:
            await asyncio.sleep(time_to_wait)  # Wait until it's time to set the item
        y_cords[i] = current_value

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
                    for item in rain_y_cords:
                        await websocket.send(str(item))
                elif message == "temp_y_cords":
                    for item in temp_y_cords:
                        await websocket.send(str(item))
            except ValueError:
                print("Error")
            else:
                tasks = [client.send(message) for client in connected_clients]
                await asyncio.gather(*tasks)
    except websockets.ConnectionClosed:
        print("Connection was closed.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Unregister the client
        connected_clients.remove(websocket)
async def server():
    start_server = await websockets.serve(echo, "0.0.0.0", 8765)
    print("Server started...")
    await start_server.wait_closed()

async def main():
    # Run both distribute_items and other_task concurrently
    await asyncio.gather(set_rain_y_cords(), set_temp_y_cords(), server(), check_date_change())

# Start the asyncio event loop
asyncio.run(main())
