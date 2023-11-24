void setup() {
  Serial.begin(9600); // Set the baud rate to 115200
}

void loop() {
  // Send a message to Python
  Serial.println("Hello from ESP32!");

  // Wait for a response from Python
  while (!Serial.available()) {
    delay(100);
  }

  // Read and print the response from Python
  String response = Serial.readString();
  Serial.print("Received from Python: ");
  Serial.println(response);

  // Add a delay before sending the next message
  delay(1000);
}