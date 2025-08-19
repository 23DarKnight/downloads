#!/usr/bin/python3
import serial
import mysql.connector
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read("/etc/parth/parth.conf")

id = config["host"]["id"]

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


def update_teams(data):
    # Database connection parameters
    dbname = 'parameters'
    user = 'gps'
    password = 'System@68'  # replace with the actual password
    host = 'localhost'  # replace with the actual host if different
    port = '3306'  # replace with the actual port if different

    try:
        # Connect to the database
        conn = mysql.connector.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            auth_plugin='mysql_native_password',
        )

        # Create a cursor object
        tid, lat, lon = data
        cur = conn.cursor()
        cur.execute("""INSERT INTO team (id, latitude, longitude) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE latitude = %s, longitude = %s; """, (tid, round(float(lat),4), round(float(lon), 4), round(float(lat),4), round(float(lon), 4)))

        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

    except mysql.connector.Error as e:
        print(f"An error occurred: {e}")




while True:
    try:
        msg = ser.readline().decode()
        if msg != "":
            print(msg)
            if ";" in msg and msg.startswith("b:"):
                msg = msg.split(";")[0]
                data = msg.split(":")
                print(data)
                update_teams(data)
    except Exception as e:
        print(e)
            
