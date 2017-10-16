from Serial import Serial
from YinBoard import YinBoard
from YangBoard import YangBoard



class ArduTermRobotTwins(object):
    """Test library for testing *Yin Yang" Arduino Scenario business logic.

    """

    def __init__(self):
        self._yin = YinBoard('/dev/ttyS0')
        self._yang = YangBoard('/dev/ttyS1')

    def setup_pin_status(self, pin, val):
        # TODO: replace following dummy code, to set the configuration of the pin
        self._yin_result = self._yin.send("print \""+pin+"="+val+"\"")

    def check_pin_status(self, pin, expected):
        # TODO: replace following dummy code, to get the status of the pin
        self._yang_result = self._yang.send("print \""+pin+"\"")
        if self._yang_result != expected_config:
            raise AssertionError('%s != %s' % (self._result, expected))


    def setup_board_configuration(self, config):
        # TODO: replace following dummy code, to set the configuration of the board
        self._yin_result = self._yin.send("print \""+config+"\"")

    def check_board_status(self, expected_config):
        # TODO: replace following dummy code, to get the status of the board
        self._yang_result = self._yang.send("print \""+config+"\"")
        if self._yang_result != expected_config:
            raise AssertionError('%s != %s' % (self._result, expected))

