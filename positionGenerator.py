import serial
import time
import random
     
adruinoSerial = serial.Serial("/dev/cu.usbmodem14201", 38400, timeout=1000)
time.sleep(2)
print("Adruino serial connection established")
posList = []

def adruinoWrite(force):
     force = round(force, 1)
     position = force * 10000
     position = position * -1 # reverse direction
     position = round(position, 1)
     position = str(position) + "\n"
     position = position.encode()
     print(position)
     adruinoSerial.write(position)

while True:
     longitudinalG = (round(random.uniform(-1, 1), 1))
     posList.append(longitudinalG)
     if len(posList) > 1000000:
          last = posList.pop()
          adruinoWrite(last)
          posList.clear()