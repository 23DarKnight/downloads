#!/usr/bin/python3
import serial
import time


# Serial connection (adjust parameters as needed)
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



gps = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)


def send_radio(msg):
    try:
        print("sending:", msg)
        ser.dtr = True  # Assert DTR for ser1 (transmit)
        ser.rts = True  # Assert RTS for ser1 (transmit)
        time.sleep(0.05)
        ser.write(f"{msg}\n".encode())
        time.sleep(0.1)
        ser.dtr = False  # Deassert DTR for ser2 (receive)
        ser.rts = False  # Deassert RTS for ser2 (receive)
    except Exception as e:
        print(e)

def get_loc(msg):
    if ";" in msg and msg.startswith("b:"):
        msg = msg.split(";")[0]
        print(msg)
        return msg

start = time.time()

msg = ""
while True:
    rcv = gps.readline().decode()
    if rcv != "":
        msg = get_loc(rcv)
    if time.time() - start > 2.5:
        send_radio(msg)
    time.sleep(0.01)



