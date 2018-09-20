# essa classe tem que: incializar serial, inicializar Protocolo e disparar cb
import threading
import asyncio

from MicrobitProtocol import MicrobitProtocol
from Serial import Serial
from constants import PORTA_SERIAL


async def _analyze_msg(line,on_message_cb):
    mib = MicrobitProtocol(line)
    if on_message_cb and mib.isValid():
        on_message_cb(mib.getMessage())

class MicrobitComm:
    def __init__(self, on_message_cb):
        self.on_message_cb = on_message_cb
        #self.serial = Serial(PORTA_SERIAL,self.on_line_received)
        self.event_loop = asyncio.new_event_loop()
        threading.Thread(target=self.event_loop.run_forever).start()

    def on_line_received(self,line):
        asyncio.run_coroutine_threadsafe(_analyze_msg(line,self.on_message_cb),loop=self.event_loop)




if __name__ == "__main__":
    mb = MicrobitComm(lambda x: print(x))
    mb.on_line_received("ANDERS:ACX72.123:ACY-12.3:OR123:ATrue:BFalse")
