from encoder import Encoder
import commands
import serial

class Transmitter:
    """
        Sends content to the led ticker device.
        - transmission is blocking
    """
    def __init__(   self,
                    device      = '/dev/ttyUSB0',
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
            self._set_device_id(device_id)

    def add_message(self, message, page):
        """ adds a message to the specified page """
        self._send_receive(commands.get_message_cmd(message, page = page))

    def set_schedule(self, pages):
        """ sets the schedule (order) of the pages """
        self._send_receive(commands.get_schedule_cmd(pages))

    def clear_screen(self):
        """ delete all pages """
        self.add_message(" ", 0)
        self.set_schedule([0])

    def delete_pages(self):
        """ delete all pages """
        self._send('<D*>')

    def end(self):
        """ terminates the connection to the led ticker """
        self.ser.close()

    def _send_receive(self, command):
        self.ser.flushInput()
        self._send(command)
        self._receive_response();

    def _send(self, command):
        """ sends a command to the device """
        data = self.encoder.encode(command)
        self._debug_log(data)

        self.ser.write(self.encoder.encode(command))

    def _receive_response(self):
        """ receives a ACK/NACK response

            ACK/NACK is sent as ascii, since its not the same length ether
            4 or 3 character are read to prevent blocking
        """
        response = self.ser.read(1)
        if response == 'N':
            chars_to_read = 3
        else:
            chars_to_read = 2
        response += self.ser.read(chars_to_read)

        self._debug_log('response: ' + response)
        return response

    def _debug_log(self, message):
        if self.debug:
            print message

    def _set_device_id(self, device_id):
        # set the device id
        self.ser.flushInput()
        self.ser.write('<ID><01><E>' + device_id)
        self._debug_log('response: ' + self.ser.read(2))

