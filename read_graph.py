import serial
import time
import signal
import threading
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval

line = [] #라인 단위로 데이터 가져올 리스트 변수

port = '/dev/ttyUSB0' # 시리얼 포트
baud = 921600 # 시리얼 보드레이트(통신속도)

exitThread = False   # 쓰레드 종료용 변수

#쓰레드 종료용 시그널 함수
def handler(signum, frame):
     exitThread = True


#데이터 처리할 함수
def parsing_data(data):
    # 리스트 구조로 들어 왔기 때문에
    # 작업하기 편하게 스트링으로 합침
    tmp = ''.join(data)
    tmp = tmp.split(',')
    #data =pd.read_csv('data4.csv')
    girox = data[1]
    giroy = data[2]
    giroz = data[3]
    accx = data[4]
    accy = data[5]
    accz = data[6]
 
    plt.cla()
    plt.plot(girox, label = 'Giro_x')
    plt.plot(giroy, label = 'Giro_y')
    plt.plot(giroz, label = 'Giro_z')
    plt.plot(accx, label = 'Acc_x')
    plt.plot(accy, label = 'Acc_y')
    plt.plot(accz, label = 'Acc_z')

    
    
    plt.legend(loc = 'upper left')
    plt.tight_layout()

#본 쓰레드
def readThread(ser):
    global line
    global exitThread

    # 쓰레드 종료될때까지 계속 돌림
    while not exitThread:
        #데이터가 있있다면
        for c in ser.read():
            #line 변수에 차곡차곡 추가하여 넣는다.
            line.append(chr(c))

            if c == 10: #라인의 끝을 만나면..
                #데이터 처리 함수로 호출
                parsing_data(line)

                #line 변수 초기화
                del line[:]                

if __name__ == "__main__":
    #종료 시그널 등록
    signal.signal(signal.SIGINT, handler)

    #시리얼 열기
    ser = serial.Serial(port, baud, timeout=0)

    #시리얼 읽을 쓰레드 생성
    thread = threading.Thread(target=readThread, args=(ser,))

    #시작!
    thread.start()
    ani = FuncAnimation(plt.gcf(),animate, interval = 1000)
    plt.tight_layout()
    plt.show()