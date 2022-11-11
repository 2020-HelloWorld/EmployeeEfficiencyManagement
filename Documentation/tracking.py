import serial
import time
import schedule
import json

def main_func():

    # arduino = serial.Serial('com5', 115200)
    # print('Established serial connection to Arduino')
    # arduino_data = arduino.readline()

    # decoded_values = str(
    #     arduino_data[0:len(arduino_data)].decode("utf-8"))
    # list_values = decoded_values.split(':')

    # for item in list_values:
    #     list_in_floats.append(item)

    # print(f'Collected readings from Arduino: {list_in_floats}')
    # for i in beacons.keys():
    #     if(i in list_in_floats[1]):
    #         beacons[i] = int(list_in_floats[0])
    # print("beacons:", beacons)
    l = ['U1\r\n', 'U2\r\n', 'U3\r\n']
    temp = []
    for i in range(3):
        temp.append(int(input()))
    global beacons
    x = 0
    for i in beacons.keys():
        beacons[i] = temp[x]
        x += 1
    temp_max = max(temp)
    res = ""
    for i in beacons.keys():
        if temp_max==beacons[i]:
            res = i
    source = -1
    # temp = max(beacons.values())
    # print(temp)
    # res = [key for key in beacons if beacons[key] == temp]
    # # print(res[0])
    
    # if(res[0] == l[0]):
    #     source = 1
    # elif(res[0] == l[1]):
    #     source = 2
    # elif(res[0] == l[2]):
    #     source = 3
    if(res == l[0]):
        source = 1
    elif(res == l[1]):
        source = 2
    elif(res == l[2]):
        source = 3
    

    # db.collection("Person").document("P-1").update({"Room": source})
    print("Room number: ",source)

    # arduino_data = 0
    # list_in_floats.clear()
    # list_values.clear()
    # arduino.close()
    print('Connection closed')
    print('<----------------------------->')

# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []
beacons = {"U1\r\n": -10000, "U2\r\n": -10000, "U3\r\n": -10000}

print('Program started')

# Setting up the Arduino
schedule.every(0.5).seconds.do(main_func)

while True:
    e = "ERROR"
    try:
        schedule.run_pending()
        time.sleep(0.5)
    except:
        print(e)
