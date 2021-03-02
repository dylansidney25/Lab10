import serial
import matplotlib.pyplot as plt
from drawnow import *

data1 = []

def PlotSignal():
    plt.ylim(0,1200)
    plt.title('ploting in streaming AD0 from arduino')
    plt.grid(True)
    plt.ylabel('analog signal AD0')
    plt.plot(data1, 'r', label='Digital Signal')
    plt.legend(loc='upper right')
    
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    plt.ion()
    Dcounter = 0
    ser.flush
    
    while True:
        while (ser.inWaiting() == 0):
            pass #do nothing if no incoming data
        ardData = ser.readline().decode('utf-8')
        InputData = ardData.split(' , ')
        temp = float(InputData[0])
        data1.append(temp)
        
        drawnow(PlotSignal)
        plt.pause(0.000001)
        Dcountr = Dcounter+1
        if(Dcounter > 60):
            DCounter = 0
            data1.pop(0)
            
    ser.close