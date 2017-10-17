from Serial import Serial
from YinBoard import YinBoard
from YangBoard import YangBoard
import logging


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



class ArduTermRobotTwins(object):
    """Test library for testing *Yin Yang" Arduino Scenario business logic.

    """

    def __init__(self):
        self._yin = YinBoard('/dev/ttyS0')
        self._yang = YangBoard('/dev/ttyS1')

    def setup_pin_mode(self, board, pin, mode):
        logger.debug(""+board+": pinmode ("+pin+", "+mode+")")
        if board=="yin":
            self._yin_result = self._yin.send("pinmode( "+pin+", "+mode+" )")
        else:
            self._yang_result = self._yang.send("pinmode( "+pin+", "+mode+" )")

    def setup_pin_status(self, board, pin, val):
        logger.debug(""+board+": d"+pin+"="+val)
        if board=="yin":
            self._yin_result = self._yin.send("d"+pin+"="+val)
        else:
            self._yang_result = self._yang.send("d"+pin+"="+val)

    def check_pin_status(self, board, pin, expected):
        if board=="yin":
            result = self._yin.send("print( d"+pin+" )")
        else:
            result = self._yang.send("print( d"+pin+" )")

        logger.debug(""+board+": d"+pin+" is "+result)
        if result != expected:
            raise AssertionError('%s != %s' % (result, expected))

    def setup_twins_pin_mode(self, pin, mode):
        modev=int(mode)
        nmodev=1-modev

        self._yin_result = self._yin.send("pinmode( "+pin+", "+modev+" )")
        self._yang_result = self._yang.send("pinmode( "+pin+", "+nmodev+" )")

    def setup_twins_pin_status(self, pin, val):
        # TODO: replace following dummy code, to set the configuration of the pin
        #self._yin_result = self._yin.send("print \""+pin+"="+val+"\"")
        pval=int(val)
        nval=1-pval
        self._yin_result = self._yin.send("d"+pin+"="+val+" )")
        self._yang_result = self._yang.send("d"+pin+"="+nval+" )")

    def check_twins_pin_status(self, pin, expected):
        # TODO: replace following dummy code, to get the status of the pin
        #self._yang_result = self._yang.send("print \""+pin+"\"")
        self._yang_result = self._yang.send("dr( d"+pin+" )")
        if self._yang_result != expected:
            raise AssertionError('%s != %s' % (self._yang_result, expected))


    def setup_board_configuration(self, config):
        # TODO: replace following dummy code, to set the configuration of the board
        self._yin_result = self._yin.send("print \""+config+"\"")

    def check_board_status(self, expected_config):
        # TODO: replace following dummy code, to get the status of the board
        self._yang_result = self._yang.send("print \""+config+"\"")
        if self._yang_result != expected_config:
            raise AssertionError('%s != %s' % (self._result, expected))

