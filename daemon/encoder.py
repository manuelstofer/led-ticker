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
            ['?','<U1B>'], ['?','<U1C>'], ['©','<U1D>'], ['?','<U1E>'], ['?','<U1F>'],
            [' ','<U20>'], ['¡','<U21>'], ['¢','<U22>'], ['£','<U23>'], ['¤','<U24>'],
            ['¥','<U25>'], ['¦','<U26>'], ['§','<U27>'], ['¨','<U28>'], ['©','<U29>'],
            ['ª','<U2A>'], ['«','<U2B>'], ['¬','<U2C>'], ['-0','<U2D>'], ['®','<U2E>'],
            ['¯','<U2F>'], ['°','<U30>'], ['±','<U31>'], ['²','<U32>'], ['³','<U33>'],
            ['´','<U34>'], ['µ','<U35>'], ['¶','<U36>'], ['·','<U37>'], ['¸','<U38>'],
            ['¹','<U39>'], ['º','<U3A>'], ['»','<U3B>'], ['¼','<U3C>'], ['½','<U3D>'],
            ['¾','<U3E>'], ['¿','<U3F>'], ['À','<U40>'], ['Á','<U41>'], ['Â','<U42>'],
            ['Ã','<U43>'], ['Ä','<U44>'], ['Å','<U45>'], ['Æ','<U46>'], ['Ç','<U47>'],
            ['È','<U48>'], ['É','<U49>'], ['Ê','<U4A>'], ['Ë','<U4B>'], ['Ì','<U4C>'],
            ['Í','<U4D>'], ['Î','<U4E>'], ['Ï','<U4F>'], ['Ð','<U50>'], ['Ñ','<U51>'],
            ['Ò','<U52>'], ['Ó','<U53>'], ['Ô','<U54>'], ['Õ','<U55>'], ['Ö','<U56>'],
            ['×','<U57>'], ['Ø','<U58>'], ['Ù','<U59>'], ['Ú','<U5A>'], ['Û','<U5B>'],
            ['Ü','<U5C>'], ['Ý','<U5D>'], ['Þ','<U5E>'], ['ß','<U5F>'], ['à','<U60>'],
            ['á','<U61>'], ['â','<U62>'], ['ã','<U63>'], ['ä','<U64>'], ['å','<U65>'],
            ['æ','<U66>'], ['ç','<U67>'], ['è','<U68>'], ['é','<U69>'], ['ê','<U6A>'],
            ['ë','<U6B>'], ['ì','<U6C>'], ['í','<U6D>'], ['î','<U6E>'], ['ï','<U6F>'],
            ['ð','<U70>'], ['ñ','<U71>'], ['ò','<U72>'], ['ó','<U73>'], ['ô','<U74>'],
            ['õ','<U75>'], ['ö','<U76>'], ['÷','<U77>'], ['ø','<U78>'], ['ù','<U79>'],
            ['ú','<U7A>'], ['û','<U7B>'], ['ü','<U7C>'], ['ý','<U7D>'], ['þ','<U7E>'],
            ['ÿ','<U7F>'] ] # http://www.danshort.com/ASCIImap/indexhex.htm

        for unsafe, safe in data:
            input_string =  re.sub(unsafe,safe,input_string)
        return input_string


