import serial
import time

# Define the serial port and baud rate
serial_port = 'COM3'  # Update with your actual COM port
baud_rate = 9600

# Create a serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    if ser.is_open:
        print(f"Connected to {serial_port} at {baud_rate} baud")

        while True:
            # Read data from the serial port
            try:
                received_data = ser.readline().decode('utf-8').strip()
                print(f"Received from ESP32: {received_data}")
            except UnicodeDecodeError as e:
                print(f"Error decoding data: {e}")
                # Print the raw byte values
                received_data = ser.readline()
                print(f"Raw data: {received_data}")

            # Send a response back to the ESP32
            ser.write(b"Hello from Python!\n")

            # Add a delay before reading the next message
            time.sleep(1)

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    # Close the serial connection
    if ser.is_open:
        ser.close()
        print("Serial connection closed")