import bluetooth
from bluetooth import *

def Connect():
    target_name = "My-Phone"
    target_address = None
    print("Before finding devices.")
    nearby_devices = discover_devices()
    print(nearby_devices)
    port = 1
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print("Before while Loop")
    while not nearby_devices:
        nearby_devices = discover_devices()
        print(f"In first while loop, Value of nearby devices is {nearby_devices}")

    for address in nearby_devices:
        if target_name == lookup_name(address):
            target_address = address
            break
        else:
            nearby_devices = discover_devices()
    if target_address is not None:
        print("found target bluetooth device with address ", target_address)
        s.connect((target_address, port))
        s.recv(1024)
        print(s)
        s.send("Hello World!")
        return True
    else:
        print("could not find target bluetooth device nearby")
        return False


TF = False
while TF is not True:
    TF = Connect()


