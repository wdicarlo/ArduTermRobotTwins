from Board import Board
from Board import Pin
from Board import DigitalPin
from Serial import Serial


class YangBoard(Board):
    def __init__(self,device):
        serial = Serial(device,57600,1)
        self._pins = [
                DigitalPin("D10","DIGITAL",10,"INPUT"),
                DigitalPin("D11","DIGITAL",11,"INPUT"),
                ]
        super(YangBoard,self).__init__("Yang",serial,[])

