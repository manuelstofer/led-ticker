from optparse import OptionParser

def get_options():
    parser = OptionParser()

    parser.add_option('-d',     '--debug',
                      dest      = 'debug',
                      action    = 'store_true',
                      help      = 'enables debug logs')

    parser.add_option('-p',     '--port',
                      dest      = 'port', 
                      default   = 3000,
                      help      = 'the port to listen on')

    parser.add_option('-b',     '--bind-interface',
                      dest      = 'interface', 
                      default   = '',
                      help      = 'bind to a specified interface, default: all')

    parser.add_option('-c',     '--console',
                      dest      = 'console',
                      action    = 'store_true',
                      help      = 'to use the server without a connected led ticker device you can output to console')

    (options, args) = parser.parse_args()
    return options
