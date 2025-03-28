import serial

print("✅ pyserial is loaded")
print(serial.__file__)
print(dir(serial))
print("💡 Creating Serial instance...")
ser = serial.Serial('COM4', 9600)  # Replace with actual COM port
print("✅ Serial connection established")
