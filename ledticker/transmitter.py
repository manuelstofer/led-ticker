from encoder import Encoder
import commands
import serial

class Transmitter:

    """ 
        Sends content to the led ticker device. 
        - transmission is blocking
    """

    def __init__(   self, 
                    device      = '/dev/tty.SLAB_USBtoUART',
                    set_id      = True,
                    device_id   = "01",
                    debug           = True,
                 ):

        self.debug = debug
        self.ser = serial.Serial(
            port            = device,
            baudrate        = 9600,
            parity          = serial.PARITY_NONE,
            stopbits        = serial.STOPBITS_ONE,
            bytesize        = serial.EIGHTBITS,
            xonxoff         = True,
        )
        self.encoder = Encoder(1)
        if set_id:
            self.set_device_id(device_id)

    def add_message(self, message, page):
        """ adds a message to the specified page """
        self._send(commands.get_message_cmd(message, page = page))

    def set_schedule(self, pages):
        """ sets the schedule (order) of the pages """
        self._send(commands.get_schedule_cmd(pages))

    def delete_pages(self):
        """ delete all pages """
        self._send('<D*>', False)

    def end(self):
        """ terminates the connection to the led ticker """
        self.ser.close()

    def _send(self, command, response = True):

        data = self.encoder.encode(command)
        self.debug_log(data)

        self.ser.flushInput()
        self.ser.write(self.encoder.encode(command))
        response = self.ser.read(1)

        if response:
            ## receive ack/nack
            if response == 'N':
                response += self.ser.read(3)
            else:
                response += self.ser.read(2)
            self.debug_log('response: ' + response)
            return response

    def debug_log(self, message):
        if self.debug:
            print message

    def set_device_id(self, device_id):
        # set the device id
        self.ser.write('<ID><01><E>' + device_id)
        self.debug_log('response: ' + self.ser.read(2))

