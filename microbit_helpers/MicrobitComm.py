# essa classe tem que: incializar serial, inicializar Protocolo
import threading
import asyncio
import serial, sys
from queue import Queue
from microbit_helpers.MicrobitProtocol import MicrobitProtocol


async def _analyze_msg(line,on_message_cb):
    mib = MicrobitProtocol(line)
    if on_message_cb and mib.isValid():
        on_message_cb(mib.getMessage())
    else:
        print("Mensagem invalida: {}", mib.getMessage())

def serial_thread(process_func):
    PORTA = sys.argv[1]
    if not PORTA:
        return

    with serial.Serial(PORTA,115200) as porta:
        while True:
            line = porta.readline().decode('UTF8').strip()
            process_func(line)

class MicrobitComm:
    def __init__(self, on_message_cb):
        self.on_message_cb = on_message_cb
        self.event_loop = asyncio.new_event_loop()
        threading.Thread(target=self.event_loop.run_forever).start()
        threading.Thread(target=serial_thread, args=[self.process]).start()


    def process(self,line):
        asyncio.run_coroutine_threadsafe(_analyze_msg(line,self.on_message_cb),loop=self.event_loop)




if __name__ == "__main__":
    mb = MicrobitComm(lambda x: print(x))
   # mb.on_line_received("ANDERS:ACX72.123:ACY-12.3:OR123:ATrue:BFalse")
