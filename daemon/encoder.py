import operator
import serial

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
        clean_command = self._clean_string(command)
        return '<ID%02X>' % self.device_id + clean_command + self._checksum(clean_command) + "<E>"

    def _checksum(self, str):
        """ returns the checksum in the expected format
            the checksum is the xor of each byte, represented as hex in ascii (2 bytes) """
        return '%02X' % reduce(operator.xor, map(ord, str))

    def _clean_string(self,input_string):
        data = [['?','<U0>'], ['  ','<U1>'],
            ['?','<U2>'], ['?','<U3>'], ['?','<U4>'], ['?','<U5>'], ['?','<U6>'],
            ['?','<U7>'], ['?','<U8>'], ['?','<U9>'], ['?','<UA>'], ['?','<UB>'],
            ['?','<UC>'], ['  ','<UD>'], ['?','<UE>'], ['  ','<UF>'], ['  ','<U10>'],
            ['?','<U11>'], ['?','<U12>'], ['?','<U13>'], ['?','<U14>'], ['?','<U15>'],
            ['?','<U16>'], ['?','<U17>'], ['?','<U18>'], ['?','<U19>'], ['?','<U1A>'],
            ['?','<U1B>'], ['?','<U1C>'], ['�','<U1D>'], ['?','<U1E>'], ['?','<U1F>'],
            [' ','<U20>'], ['�','<U21>'], ['�','<U22>'], ['�','<U23>'], ['�','<U24>'],
            ['�','<U25>'], ['�','<U26>'], ['�','<U27>'], ['�','<U28>'], ['�','<U29>'],
            ['�','<U2A>'], ['�','<U2B>'], ['�','<U2C>'], ['-0','<U2D>'], ['�','<U2E>'],
            ['�','<U2F>'], ['�','<U30>'], ['�','<U31>'], ['�','<U32>'], ['�','<U33>'],
            ['�','<U34>'], ['�','<U35>'], ['�','<U36>'], ['�','<U37>'], ['�','<U38>'],
            ['�','<U39>'], ['�','<U3A>'], ['�','<U3B>'], ['�','<U3C>'], ['�','<U3D>'],
            ['�','<U3E>'], ['�','<U3F>'], ['�','<U40>'], ['�','<U41>'], ['�','<U42>'],
            ['�','<U43>'], ['�','<U44>'], ['�','<U45>'], ['�','<U46>'], ['�','<U47>'],
            ['�','<U48>'], ['�','<U49>'], ['�','<U4A>'], ['�','<U4B>'], ['�','<U4C>'],
            ['�','<U4D>'], ['�','<U4E>'], ['�','<U4F>'], ['�','<U50>'], ['�','<U51>'],
            ['�','<U52>'], ['�','<U53>'], ['�','<U54>'], ['�','<U55>'], ['�','<U56>'],
            ['�','<U57>'], ['�','<U58>'], ['�','<U59>'], ['�','<U5A>'], ['�','<U5B>'],
            ['�','<U5C>'], ['�','<U5D>'], ['�','<U5E>'], ['�','<U5F>'], ['�','<U60>'],
            ['�','<U61>'], ['�','<U62>'], ['�','<U63>'], ['�','<U64>'], ['�','<U65>'],
            ['�','<U66>'], ['�','<U67>'], ['�','<U68>'], ['�','<U69>'], ['�','<U6A>'],
            ['�','<U6B>'], ['�','<U6C>'], ['�','<U6D>'], ['�','<U6E>'], ['�','<U6F>'],
            ['�','<U70>'], ['�','<U71>'], ['�','<U72>'], ['�','<U73>'], ['�','<U74>'],
            ['�','<U75>'], ['�','<U76>'], ['�','<U77>'], ['�','<U78>'], ['�','<U79>'],
            ['�','<U7A>'], ['�','<U7B>'], ['�','<U7C>'], ['�','<U7D>'], ['�','<U7E>'],
            ['�','<U7F>'] ] # http://www.danshort.com/ASCIImap/indexhex.htm

        for unsafe, safe in data:
            input_string =  re.sub(unsafe,safe,input_string)
        return input_string


