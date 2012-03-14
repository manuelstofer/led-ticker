
import time
import sys
import ledticker

from twisted.internet import protocol, reactor
from twisted.application import service, internet

transmitter = ledticker.Transmitter()

factory = protocol.ServerFactory()
factory.protocol = ledticker.TwistedAdapter
factory.queue    = ledticker.MessageQueue(transmitter)

reactor.listenTCP(3000,factory)
reactor.run()

# application = service.Application("tickerserver")
# internet.TCPServer(3000, factory).setServiceParent(application)

