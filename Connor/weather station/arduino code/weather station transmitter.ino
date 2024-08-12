#include <Wire.h>
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <avr/wdt.h> // Include watchdog timer library
#include "SparkFunMPL3115A2.h"
#include "SparkFun_Si7021_Breakout_Library.h"
#include "SparkFun_Weather_Meter_Kit_Arduino_Library.h"

#define status_led_1 7
#define status_led_2 8
#define power_reference A3
#define input_voltage_reference A2

long ms_counter;
const byte address[6] = "00001";

MPL3115A2 pressure_sensor;
SI7021 humidity_sensor;
SFEWeatherMeterKit waterproof_sensors(A0, 3, 2); // wind direction pin is A0, wind speed pin is D3 and rain pin is D2
RF24 transceiver(9, 10); // ce = D9, csn = D10

void setup() {
  Serial.begin(9600);
  Wire.begin();
  pinMode(status_led_1, OUTPUT);
  pinMode(status_led_2, OUTPUT);
  pinMode(power_reference, INPUT);

  pressure_sensor.begin();
  pressure_sensor.setModeBarometer();
  pressure_sensor.setOversampleRate(7);
  pressure_sensor.enableEventFlags();

  humidity_sensor.begin();
  waterproof_sensors.setADCResolutionBits(10);
  waterproof_sensors.begin();

  transceiver.begin();
  transceiver.setPALevel(RF24_PA_HIGH);
  transceiver.openWritingPipe(address);
  transceiver.openReadingPipe(1, address); // Open another pipe for receiving
  transceiver.startListening(); // Start listening for incoming data

  ms_counter = millis();
}

void loop() {
  // Check if data is available from the receiver
  if (transceiver.available()) {
    char received_data[255] = "";
    transceiver.read(received_data, sizeof(received_data) - 1); // Read incoming data
    received_data[sizeof(received_data) - 1] = '\0'; // Ensure null termination

    Serial.print("Received data: ");
    Serial.println(received_data);

    // Process received data
    if (strcmp(received_data, "r") == 0) {
      Serial.println("Reset command received. Activating watchdog timer.");
      delay(1000);
      wdt_enable(WDTO_15MS); // Enable watchdog timer with 15 ms timeout
      while (1) { /* Wait for watchdog to reset the Arduino */ }
    }
  }

  // Send data every 2 seconds
  if (millis() - ms_counter >= 2000) {
    digitalWrite(status_led_1, HIGH);
    ms_counter += 2000;

    doweathercalc();
    digitalWrite(status_led_1, LOW);
  }

  delay(100);
}

void doweathercalc() {
  float humidity = humidity_sensor.getRH();
  float temp = humidity_sensor.readTemp();
  float wind_dir = waterproof_sensors.getWindDirection();
  float wind_speed = waterproof_sensors.getWindSpeed();
  float rainMM = waterproof_sensors.getTotalRainfall();
  float pressure = pressure_sensor.readPressure();
  float working_voltage = analogRead(power_reference);
  float input_voltage = analogRead(input_voltage_reference);
  working_voltage = 3.30 / working_voltage;
  input_voltage *= working_voltage;
  input_voltage *= 4.90;

  String data1 = String("H=") + String(humidity, 1) +
                  ",T=" + String(temp, 1) +
                  ",P=" + String(pressure, 1) +
                  ",W=" + String(wind_speed, 1);
  String data2 = String("D=") + String(wind_dir, 1) +
                  ",R=" + String(rainMM, 1) +
                  ",B=" + String(input_voltage, 2);

  bool transmit_success1 = sendData(data1);
  delay(400);
  bool transmit_success2 = sendData(data2);

  if (transmit_success1 || transmit_success2) {
    digitalWrite(status_led_2, HIGH);
    delay(50);
    digitalWrite(status_led_2, LOW);
  }
  Serial.print(data1);
  Serial.println(data2);
}

bool sendData(String data) {
  transceiver.stopListening(); // Stop listening before sending
  bool success = transceiver.write(data.c_str(), data.length() + 1); // Send data
  transceiver.startListening(); // Start listening again
  return success;
}
