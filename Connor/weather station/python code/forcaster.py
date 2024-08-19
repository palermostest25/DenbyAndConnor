import time
import random
import numpy as np

class rain_forcast:
    def __init__(self):
        self.pressure_trend = []
        self.forecast = "Unknown"
    
    def update_sensors(self, pressure, temperature, humidity, wind_speed, rainfall):
        self.pressure_trend.append(pressure)
        if len(self.pressure_trend) > 720:  # Keep the last 2 hours of data (720 samples)
            self.pressure_trend.pop(0)
        
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.rainfall = rainfall
        
        self.forecast = self.forecast_weather()

    def forecast_weather(self):
        if len(self.pressure_trend) < 2:
            return "Data insufficient for forecasting"

        pressures = np.array(self.pressure_trend)
        time_indices = np.arange(len(pressures))

        # Calculate slope of the pressure trend using linear regression
        slope, _ = np.polyfit(time_indices, pressures, 1)
        print(slope)
        # Analyze the trend
        forecast = "Weather stable"
        
        if slope > 5:  # Arbitrary threshold for increasing pressure
            forecast = "Improving weather - Sunny/Clear"
        elif slope < -5:  # Arbitrary threshold for decreasing pressure
            forecast = "Worsening weather - Rain/Storm likely"
        
        # Additional checks for rapid changes
        pressure_change = pressures[-1] - pressures[0]
        if pressure_change < -5 and self.wind_speed > 15:
            forecast = "Mild storm incomming"

        if pressure_change < -12 and self.wind_speed > 15:
            forecast = "Severe storm incomming"

        return forecast

    def get_forecast(self):
        return self.forecast

# Simulate the weather station updating every 10 seconds
rain_forcast = rain_forcast()

for _ in range(720):  # Simulate for 2 hours (720 * 10 seconds)
    pressure = random.uniform(1005, 1020)  # Simulate pressure reading
    print(pressure)
    temperature = random.uniform(-5, 20)  # Simulate temperature reading
    humidity = random.uniform(40, 100)  # Simulate humidity reading
    wind_speed = random.uniform(0, 25)  # Simulate wind speed
    rainfall = random.uniform(0, 10) if random.random() > 0.8 else 0  # Simulate occasional rainfall
    
    rain_forcast.update_sensors(pressure, temperature, humidity, wind_speed, rainfall)
    print(f"Current Forecast: {rain_forcast.get_forecast()}")
    
    time.sleep(10)  # Wait for 10 seconds before the next update
