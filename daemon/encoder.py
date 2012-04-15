import operator
import serial

import commands

class Encoder:

    def __init__(self, device_id):
        self.device_id = device_id

    def encode(self, command):
        """ all commands sent to the device are wrapped with the following format:

            <IDx>       the device id (multiple devices are possible)
            command     the commands
            checksum    a xor checksum of the commands represented hex in ascii
            <E>         terminates the commands
        """
        return '<ID%02X>' % self.device_id + command + self._checksum(command) + "<E>"

    def _checksum(self, str):
        """ returns the checksum in the expected format
            the checksum is the xor of each byte, represented as hex in ascii (2 bytes) """
        return '%02X' % reduce(operator.xor, map(ord, str))

