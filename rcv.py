import serial
import time


ser = serial.Serial(
    port='/dev/ttyUSB0',  # Adjust the port to match your device
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    xonxoff=False,  # Disable software flow control
    rtscts=False,   # Disable hardware (RTS/CTS) flow control
    dsrdtr=False,   # Disable DSR/DTR flow control
    timeout=0.1
)
ser.dtr = False  # Deassert DTR for ser2 (receive)
ser.rts = False  # Deassert RTS for ser2 (receive)



while True:
    msg = ser.readline()
    if msg != "":
        print(msg)
