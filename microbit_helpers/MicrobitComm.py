# essa classe tem que: incializar serial, inicializar Protocolo
import threading
import asyncio
import serial, sys
import time
import array
from queue import Queue
from microbit_helpers.MicrobitProtocol import MicrobitProtocol

fila_msg = Queue()

def serial_thread(process_func):
    PORTA = sys.argv[1]
    if not PORTA:
        return
    #threading.Thread(target=process_msg_thread, args=[process_func]).start()

    with serial.Serial(PORTA,115200,timeout=None) as porta:
        arr = bytearray(251)
        while True:
            # i =0
            # while True:
            #     b = porta.read()
            #     if b == None or b == b'\x00' or b == b'\x01' or b == b'':
            #         continue
            #     elif b == b'\n' :
            #         break
            #     else:
            #         arr[i] = b[0]
            #         i += 1
            #print(arr[:i])
            line = porta.readline()
            if line[0] == 1 and line[1] == 0 and line[2] == 1: 
                msg = line[3:].decode('ascii').strip()
                process_func(msg)


#def process_msg_thread(process_func):
  #  while True:
        #if not fila_msg.empty():
        #    line = fila_msg.get()
       #     msg =
       # time.sleep(0.001)


class MicrobitComm:
    def __init__(self, on_message_cb):
        self.on_message_cb = on_message_cb
        threading.Thread(target=serial_thread, args=[self.process]).start()


    def process(self,line):
        mib = MicrobitProtocol(line)
        if self.on_message_cb and mib.isValid():
            self.on_message_cb(mib.getMessage())
        else:
            print("Mensagem invalida:", mib.getMessage())




if __name__ == "__main__":
    mb = MicrobitComm(lambda x: print(x))
   # mb.on_line_received("ANDERS:ACX72.123:ACY-12.3:OR123:ATrue:BFalse")
