#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 transceiver(7, 8); // ce = D7, csn = D8

const byte address[6] = "00001";
long counter;
bool reset;

void setup() {
  Serial.begin(9600);
  reset = true;
  transceiver.begin();
  transceiver.setPALevel(RF24_PA_HIGH);

  // Setup for sending and receiving
  transceiver.openWritingPipe(address); // Set address for sending
  transceiver.openReadingPipe(1, address); // Set address for receiving
  transceiver.startListening(); // Start listening for incoming data
}

void loop() {
  if (transceiver.available()) {
    // Receive the first piece of data
    char data1[255] = "";
    transceiver.read(data1, sizeof(data1) - 1); 
    data1[sizeof(data1) - 1] = '\0';  // Ensure null termination

    delay(500); // Wait before receiving the second piece of data

    // Receive the second piece of data
    char data2[255] = "";
    transceiver.read(data2, sizeof(data2) - 1); 
    data2[sizeof(data2) - 1] = '\0';  // Ensure null termination

    // Combine both pieces of data into a single string
    String data = String(data1) + "," + String(data2);
    Serial.println(data);  // Print the combined data to Serial Monitor

    // Check if received data matches a specific condition
    if (reset) {
      sendResetCommand();
      reset = false;
    }
  }

  delay(100); // Adjust as needed
}

void sendResetCommand() {
  transceiver.stopListening(); // Stop listening before sending
  const char resetCommand[] = "r";
  bool success = transceiver.write(resetCommand, sizeof(resetCommand)); // Send "r"
  
  if (success) {
    Serial.println("Reset command sent successfully.");
  } else {
    Serial.println("Failed to send reset command.");
  }
  
  transceiver.startListening(); // Start listening again
}
