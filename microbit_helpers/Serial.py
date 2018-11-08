import serial , threading


def _serial(serial,cb):
    print("Inicializou")
    while True:
        msg = str(serial.readline(), encoding='UTF-8')
        if msg and cb:
            cb(msg)


class Serial:
    def __init__(self, porta, on_line_cb):
        self.porta = serial.Serial('COM6', 115200)
        #self.on_line_cb = on_line_cb;
        self.thread = threading.Thread(target=_serial,args=(serial,on_line_cb))
        self.thread.start()


