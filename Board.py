from Serial import Serial

class Pin(object):
    def __init__(self,name,pintype,pinid):
        self._name = name
        self._pintype = pintype # TODO: use an enum
        self._pinid = pinid

class DigitalPin(Pin):
    def __init__(self,name,pintype,pinid,mode):
        self._isInput = False
        if mode == "INPUT":
            self._isInput = True
        super(DigitalPin,self).__init__(name,pintype,pinid)


class Board(object):
    def __init__(self, name, serial, pins):
        if isinstance(serial,Serial) == False: 
            raise ValueError("Bad Serial")
        # TODO: check pins
        #if isinstance(pins,Pin) == False: 
        #    raise ValueError("Bad Pins")
        self._serial = serial
        self._name = name
        self._pins = pins


    def send(self,msg):
        return self._serial.send(msg)

    def set_pin(pin,val):
        pass
    def get_pin(pin):
        pass
