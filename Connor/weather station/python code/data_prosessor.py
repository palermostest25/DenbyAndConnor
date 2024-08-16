import re 
import asyncio
import websockets

async def send_data(H, T, P, W, D, R, B, uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("start")
        await websocket.send(H)
        await websocket.send(T)
        await websocket.send(P)
        await websocket.send(W)
        await websocket.send(D)
        await websocket.send(R)
        await websocket.send(B)
        await websocket.send("end")
        while not await websocket.recv() == "end":
            pass
async def receive_data(uri):
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                try:
                    # Wait for a message with a timeout
                    response = await asyncio.wait_for(websocket.recv(), timeout=1.0)  # 1 second timeout
                    if response == "r":
                        print("Reset Arduino")
                        break
                except asyncio.TimeoutError:
                    # Handle the timeout case (e.g., periodic check or log)
                    print("No data received")
                    break
                except websockets.ConnectionClosed:
                    print("Connection closed.")
                    break
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    uri = "wss://weatherstationserver.moahub.org/"
    while True:
        working_data = input("Input working data: ")
        if len(working_data) > 40:
            working_humidity = re.search(r"H=\d{1,3}\.\d", working_data)
            working_humidity = working_humidity.group()
            working_humidity = working_humidity.split("=")
            working_humidity = working_humidity[1]
            print(f"Working humidity = {working_humidity}%")
            working_temp = re.search(r"T=\d{1,2}\.\d", working_data)
            working_temp = working_temp.group()
            working_temp = working_temp.split("=")
            working_temp = working_temp[1]
            print(f"Working temp = {working_temp}°C")
            working_pressure = re.search(r"P=\d{1,6}\.\d", working_data)
            working_pressure = working_pressure.group()
            working_pressure = working_pressure.split("=")
            working_pressure = working_pressure[1]
            try:
                working_pressure = float(working_pressure)
                working_pressure = working_pressure / 100
                working_pressure = str(working_pressure)
                working_pressure = working_pressure.split(".")
                working_pressure = working_pressure[0]
                print(f"Working pressure = {working_pressure}kPa")
            except Exception as e:
                print(f"Error: {e}")
                print(f"Working pressure = {working_pressure}Pa")
            working_w_spd = re.search(r"W=\d{1,2}\.\d", working_data)
            working_w_spd = working_w_spd.group()
            working_w_spd = working_w_spd.split("=")
            working_w_spd = working_w_spd[1]
            print(f"Working wind speed = {working_w_spd}KPH")
            working_w_dir = re.search(r"D=\d{1,3}", working_data)
            working_w_dir = working_w_dir.group()
            working_w_dir = working_w_dir.split("=")
            working_w_dir = working_w_dir[1]
            print(f"Working wind direction = {working_w_dir}°")
            working_rain = re.search(r"R=\d{1,3}\.\d", working_data)
            working_rain = working_rain.group()
            working_rain = working_rain.split("=")
            working_rain = working_rain[1]
            print(f"Working rain = {working_rain}MM")
            working_input_voltage = re.search(r"B=\d{1,2}\.\d{1,2}", working_data)
            working_input_voltage = working_input_voltage.group()
            working_input_voltage = working_input_voltage.split("=")
            working_input_voltage = working_input_voltage[1]
            print(f"Working input voltage = {working_input_voltage}V")
            await receive_data(uri)
            await send_data(working_humidity, working_temp, working_pressure, working_w_spd, working_w_dir, working_rain, working_input_voltage, uri)
        else:
            print("Not enough data")
asyncio.run(main())
