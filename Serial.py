import serial
import time
import signal
import sys
import array
import re
import atexit
import logging

ARDUINO_PROMPT='>'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('serial.log')
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class Serial(object):

    def __init__(self,device,speed,stimeout):
        #logging.basicConfig(filename="arduino_serial.log",level=logging.DEBUG)
        #logging.getLogger().addHandler(logging.FileHandler("log.txt"))
        logger.debug("Begin of Serial execution")

        logger.debug("Installing CTRL-C handler...")
        signal.signal(signal.SIGINT, self.signal_handler)

        logger.debug("Connecting to serial...")
        #self._arduino = serial.Serial('/dev/ttyS0',9600,timeout=2)
        #self._arduino = serial.Serial('/dev/ttyS0',19200,timeout=1)
        #self._arduino = serial.Serial('/dev/ttyS0',38400,timeout=1)
        #self._arduino = serial.Serial('/dev/ttyS0',57600,timeout=1)
        #self._arduino = serial.Serial('/dev/ttyS0',115000,timeout=1)
        self._arduino = serial.Serial(device,speed,timeout=stimeout)
        time.sleep(1)
        #self._arduino.write(b'\r')

        self._matcher = re.compile(r'^'+ARDUINO_PROMPT)
        atexit.register(self.cleanup)
        logger.debug(self.receive())
        logger.debug("End of Serial initialization.")

    def cleanup(self):
        logger.debug("Running cleanup...")
        self._arduino.close()
        logger.debug("End of serial execution")

    def signal_handler(self, signal, frame):
            logger.debug('You pressed Ctrl+C!')
            logger.debug("bye")
            self._arduino.close()
            sys.exit(0)

    def receive(self):
        eot=False
        response=''
        maxemptylines=3
        emptylines=0
        numlines=0
        while(not eot):
            line = self._arduino.readline().strip()
            numlines = numlines + 1
            logger.debug("Arduino Line: "+line)
            #logger.debug("Arduino Line ("+len(line)+"): "+line)
            if len(line) == 0:
                emptylines=emptylines+1
                res = False
                if emptylines == maxemptylines:
                    eot = True
                    emptylines = 0
                    logger.debug("Too many empty lines")
            else:
                res = bool(self._matcher.findall(line))
            if res:
                eot = True # reached prompt, so quit
            if len(line) > 0 and numlines > 1 and line[0] != '\n' and line[0] != '>':
                logger.debug("Arduino Appending: "+line)
                response = response + line
        logger.debug("Arduino Response: "+response)
        return response

    def send(self,msg):
        logger.debug("Sending message: "+msg)
        # send command
        self._arduino.write(msg.encode())
        self._arduino.write(b'\r')
        #time.sleep(1)
        #self._arduino.flush()
        # read the response
        return self.receive()
