import minimalmodbus
import time

servoDrive = minimalmodbus.Instrument('/dev/cu.usbserial-A704FRNP', 1)
servoDrive.serial.baudrate = 38400
servoDrive.close_port_after_each_call = True


def parameterInitialize():
    try:
        servoDrive.write_register(2, 1, functioncode=6) # P0-02 Parameter Initialization 
        #servoDrive.write_register(3, 1, functioncode=6) # P0-03 Software Reset
        print("Parameter Initialization successful")
    except IOError:
        print("Parameter Initialization failed", IOError)


def positionControlMode():
    try:
        servoDrive.write_register(260, 1, functioncode=6) # P1-04 Internal Servo Start
        servoDrive.write_register(256, 0, functioncode=6) # P1-00 Control Mode (External Instruction Pulse Input) 
        print("Positon control settings successful")
    except IOError:
        print("Positon control settings failed", IOError)        

def servoTuning():
    try:
        # 1. Pulse multiplikator
        servoDrive.write_register(262, 5, functioncode=6)

        # 2. Smoothing
        #servoDrive.write_register(535, 2, functioncode=6)

        # 3. Smoothing Filter Time?

        # 4. Feedforward %
        #servoDrive.write_register(516, 200, functioncode=6)

        # 5. Gain % (need to match attribute)
        # servoDrive.write_register(514, 200, functioncode=6)

        print("Servo tuning successful")
    except IOError:
        print("Servo tuning failed", IOError)


def positionControlInit():
    parameterInitialize()
    time.sleep(1)

    positionControlMode()
    time.sleep(1)

    servoTuning()
    time.sleep(1)


positionControlInit()