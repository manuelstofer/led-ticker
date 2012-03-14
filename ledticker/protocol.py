from twisted.protocols import basic
from twisted.internet import reactor

class TwistedAdapter(basic.LineReceiver):
    """
        Line based adapter for twisted
    """
    def lineReceived(self, line):
        self.factory.queue.add_message(line)
