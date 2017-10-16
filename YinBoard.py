from Board import Board
from Board import Pin
from Board import DigitalPin
from Serial import Serial

class YinBoard(Board):
    def __init__(self,device):
        serial = Serial(device,57600,1)
        self._pins = [
                DigitalPin("D01","DIGITAL",1,"OUTPUT"),
                DigitalPin("D02","DIGITAL",1,"OUTPUT"),
                ]

        super(YinBoard,self).__init__("Yin",serial,self._pins)

