
from transmitter        import Transmitter
from messagethrottler   import MessageThrottler
from twistedadapter     import TwistedAdapter

import time
import sys
from twisted.internet import protocol, reactor
from twisted.application import service, internet
import options

options = options.get_options()

if not options.console:
    Transmitter = Transmitter
else:
    Transmitter = DebugTransmitter


transmitter = Transmitter(
    debug = options.debug
)

# setup factory for twisted
factory = protocol.ServerFactory()
factory.protocol = TwistedAdapter
factory.queue    = MessageThrottler(transmitter)

# run in twisted
reactor.listenTCP(
    int(options.port),
    factory, 
    interface = options.interface
)
reactor.run()

