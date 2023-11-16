import serial

ser = serial.Serial('COM4', 9600) # Replace with the correct serial port and baud rate for your RFID reader

while True:
    data = ser.readline()
    if data:
        tag_data = data.decode().strip().split(',')
        if len(tag_data) >= 2:
            tag_id, signal_strength = tag_data[:2]
            print(f"Tag ID: {tag_id}, Signal Strength: {signal_strength},Scanner name:{serial.println('Techpark')}")


