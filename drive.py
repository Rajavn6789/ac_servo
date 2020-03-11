import minimalmodbus
import time

servoDrive = minimalmodbus.Instrument('/dev/cu.usbserial-A704FRNP', 1)
servoDrive.serial.baudrate = 38400
servoDrive.close_port_after_each_call = True


def speedControl():
    try:
        servoDrive.write_register(256, 2, functioncode=6) # P1-00 Control Mode 
        servoDrive.write_register(257, 1, functioncode=6) # P1-01 Input Polarity  
        servoDrive.write_register(259, 1, functioncode=6) # P1-03 Input Source 
        servoDrive.write_register(260, 1, functioncode=6) # P1-04 Internal Servo Start
        servoDrive.write_register(1068, 100, functioncode=6) # P4-44
        print("Write successful")
    except IOError:
        print("Failed to read from instrument", IOError)


def parameterInitialize():
    try:
        servoDrive.write_register(2, 1, functioncode=6) # P0-02 Parameter Initialization 
        servoDrive.write_register(3, 1, functioncode=6) # P0-03 Software Reset
        print("Initialization successful")
    except IOError:
        print("Failed to read from instrument", IOError)


def positionControlMode():
    try:
        servoDrive.write_register(260, 1, functioncode=6) # P1-04 Internal Servo Start
        servoDrive.write_register(256, 0, functioncode=6) # P1-00 Control Mode (External Instruction Pulse Input) 
        print("Write successful")
    except IOError:
        print("Failed to read from instrument", IOError)        

'''
def logPositionParameters():
    try:
        print("P1-06", servoDrive.read_register(262)) # P1-06 PElectronic Gear Ratio Numerator
        print("P2-23", servoDrive.read_register(535)) # P2-23 Position Instruction Smoothing Function Selection
        print("P2-04", servoDrive.read_register(516)) # P2-04 Position Control Feed forward Gain
        print("P2-02", servoDrive.read_register(514)) # P2-02 Position Control Proportional Gain
    except IOError:
        print("Failed to read from instrument", IOError)
'''

def servoTuning():
    try:
        # 1. Pulse multiplikator
        servoDrive.write_register(262, 5, functioncode=6)

        # 2. Smoothing
        #servoDrive.write_register(535, 2, functioncode=6)

        # 3. Smoothing Filter Time?

        # 4. Feedforward %
        #servoDrive.write_register(516, 200, functioncode=6)
    except IOError:
        print("Failed to write to drive", IOError)

parameterInitialize()
time.sleep(1)

positionControlMode()
time.sleep(1)

# logPositionParameters()
#time.sleep(1)

servoTuning()
time.sleep(1)
