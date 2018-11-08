import re
from microbit_helpers.Message import Message

class MicrobitProtocol:
    _REGEX_PROTOCOL = re.compile(
        "^([a-zA-Z]{1,7}):ACX(-?\d+|-?\d+.{1}\d+):ACY(-?\d+|-?\d+.{1}\d+):OR(-?\d+|-?\d+.{1}\d+):A(False|True):B(False|True)$")
    _USERNAME_GROUP = 1
    _ACC_X_GROUP = 2
    _ACC_Y_GROUP = 3
    _ORIENTATION_GROUP = 4
    _A_PRESS_GROUP = 5
    _B_PRESS_GROUP = 6

    def __init__(self,line):
        self.is_valid = False
        match = MicrobitProtocol._REGEX_PROTOCOL.match(line)
        if match:
            self.is_valid = True
            self.msg = Message(
                match.group(MicrobitProtocol._USERNAME_GROUP),
                acc_x=match.group(MicrobitProtocol._ACC_X_GROUP),
                acc_y=match.group(MicrobitProtocol._ACC_Y_GROUP),
                orientation=match.group(MicrobitProtocol._ORIENTATION_GROUP),
                a_press=match.group(MicrobitProtocol._A_PRESS_GROUP),
                b_press=match.group(MicrobitProtocol._B_PRESS_GROUP)
            )
        else:
            self.msg = line
    def isValid(self):
        return self.is_valid

    def getMessage(self):
        return self.msg