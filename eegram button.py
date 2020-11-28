#Serial communication
import serial
import time
import sys

def setup():
    serial.begin(115200)

def loop():
    atr_signal_data = analogRead(A0) # in here goes pin for atr_signal
    vent_signal_data = analogRead(A1) # in here goes pin for vent_signal
    serial.println(atr_signal_data, vent_signal_data)

def egram(self):
    # command to bring control here when egram button pressed
    #done

    # when this function is called, something in stateflow is triggered to be sending natural signals from pins A0 and A1
    # (from heartview) out, so that when serial.read is called, we are receiving the correct data (art and vent signal)
    # every timestamp, stateflow will send a value (every second or something for 10s) = our 10 data points.
    # we have to have a method to stop data streaming too

    # requesting data values
    ser = serial.Serial('COM6', baudrate=115200, timeout=1)

    while 1:
        data_pt = ser.readline().decode('ascii')
        print(data_pt)

    vent_egram = []
    atr_egram = []
    arr = []

    # creating placeholder array with definite size for each parameter we are sending/receiving
    for person in range(10):
        arr.append('b\x01') #first byte det if you want to update values (0x55), or get eegram (0x22)
        arr.append('b\x')
        for parameter in range(22):
            arr.append('b\x0f')
        arr.append('b\x15')

    # sending current data to board
    for j in arr:
        ser.write(j)

    i = 1
    while i:  # Reading Vent. and Atr. serial data

        s = ser.read() # reads data from port from computer --> stateflow must be sending data from pacemaker shield (A0 and A1)
        s = int.from_bytes(s, byteorder=sys.byteorder)
        serialArrayIn.append(s)

        i += 1
        if i > 22:
            i = 0

    time.sleep(0.5)

    vent_egram.append(serialArrayIn[24])
    atr_egram.append(serialArrayIn[23])

    plt.figure(1)
    plt.subplot(211)
    plt.xlabel('time')
    plt.ylabel("Vent. Egram")
    plt.plot(vent_egram)

    plt.subplot(212)
    plt.ylabel("Atr. Egram")
    plt.xlabel('time')
    plt.plot(atr_egram)
    plt.show()
