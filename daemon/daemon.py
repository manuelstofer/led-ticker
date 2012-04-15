
import ledticker
import time
import sys
from twisted.internet import protocol, reactor
from twisted.application import service, internet
import options

options = options.get_options()

if not options.console:
    Transmitter = ledticker.Transmitter
else:
    Transmitter = ledticker.DebugTransmitter


transmitter = Transmitter(
    debug = options.debug
)

# setup factory for twisted
factory = protocol.ServerFactory()
factory.protocol = ledticker.TwistedAdapter
factory.queue    = ledticker.MessageThrottler(transmitter)

# run in twisted
reactor.listenTCP(
    int(options.port),
    factory, 
    interface = options.interface
)
reactor.run()

