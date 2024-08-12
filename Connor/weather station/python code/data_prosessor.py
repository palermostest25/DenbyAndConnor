import re 

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
    else:
        print("Not enough data")
