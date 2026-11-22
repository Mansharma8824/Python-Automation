import sys

# check the version
print(sys.version)

# used to work with command line arguments
print("Aguments", sys.argv)
device_name = sys.argv[1]
protocol = sys.argv[2]

print("testing device", device_name)
print("Protocol", protocol)

# sys.exit()
# Used to terminate a Python script
device_connected = False
if not device_connected:
    print("Device connection failed")
    sys.exit(1)
print("Running device test")

