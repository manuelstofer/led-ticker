
import ledticker
import time
import sys
from optparse import OptionParser
from twisted.internet import protocol, reactor
from twisted.application import service, internet


# parse options
parser = OptionParser()
parser.add_option("-d",     '--debug',
                  dest      = "debug",
                  action    = "store_true",
                  help      = "to use the server without having the device connected you can log to std")

(options, args) = parser.parse_args()


## instanciate transmitter
if not options.debug:
    transmitter = ledticker.Transmitter() 
else:
    transmitter = ledticker.DebugTransmitter()

# setup factory for twisted
factory = protocol.ServerFactory()
factory.protocol = ledticker.TwistedAdapter
factory.queue    = ledticker.MessageQueue(transmitter)

# run in twisted
reactor.listenTCP(3000,factory)
reactor.run()

