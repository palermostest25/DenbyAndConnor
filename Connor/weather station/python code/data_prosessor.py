import re
import asyncio
import websockets
import serial

def read_and_write_to_serial(port='/dev/ttyACM0', baudrate=9600, timeout=1, command=None):
    try:
        ser = serial.Serial(port, baudrate, timeout=timeout)
        if command:
            ser.write((command + "\n").encode('utf-8'))
        elif ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            return data
        return None
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        return None
    finally:
        ser.close()

async def send_data(H, T, P, W, D, R, B, websocket):
    await websocket.send("start")
    await websocket.send(H)
    await websocket.send(T)
    await websocket.send(P)
    await websocket.send(W)
    await websocket.send(D)
    await websocket.send(R)
    await websocket.send(B)
    await websocket.send("end")
    while await websocket.recv() != "end":
        pass

async def receive_data(websocket):
    while True:
        try:
            response = await asyncio.wait_for(websocket.recv(), timeout=1.0)
            if response == "r":
                read_and_write_to_serial(command='r')
                break
        except asyncio.TimeoutError:
            print("No data received")
            break

async def main():
    uri = "wss://weatherstationserver.moahub.org/"
    while True:
        async with websockets.connect(uri) as websocket:
            while True:
                working_data = read_and_write_to_serial()
                if working_data is None:
                    await asyncio.sleep(0.1)
                    continue
                if len(working_data) > 40:
                    working_humidity = re.search(r"H=\d{1,3}\.\d", working_data).group().split("=")[1]
                    print(f"Working humidity = {working_humidity}%")
                    working_temp = re.search(r"T=\d{1,2}\.\d", working_data).group().split("=")[1]
                    print(f"Working temp = {working_temp}°C")
                    working_pressure = re.search(r"P=\d{1,6}\.\d", working_data).group().split("=")[1]
                    try:
                        working_pressure = str(float(working_pressure) / 100).split(".")[0]
                        print(f"Working pressure = {working_pressure}kPa")
                    except Exception as e:
                        print(f"Error: {e}")
                        print(f"Working pressure = {working_pressure}Pa")
                    working_w_spd = re.search(r"W=\d{1,2}\.\d", working_data).group().split("=")[1]
                    print(f"Working wind speed = {working_w_spd}KPH")
                    working_w_dir = re.search(r"D=\d{1,3}", working_data).group().split("=")[1]
                    print(f"Working wind direction = {working_w_dir}°")
                    working_rain = re.search(r"R=\d{1,3}\.\d", working_data).group().split("=")[1]
                    print(f"Working rain = {working_rain}MM")
                    working_input_voltage = re.search(r"B=\d{1,2}\.\d{1,2}", working_data).group().split("=")[1]
                    print(f"Working input voltage = {working_input_voltage}V")
                    try:
                        await receive_data(websocket)
                        await send_data(working_humidity, working_temp, working_pressure, working_w_spd, working_w_dir, working_rain, working_input_voltage, websocket)
                    except Exception as e:
                        print("Error while processing websocket communication:", e)
                    except websockets.ConnectionClosed:
                        break
                else:
                    print("Not enough data")

asyncio.run(main())
