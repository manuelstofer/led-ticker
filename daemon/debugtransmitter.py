class DebugTransmitter:

    def __init__(   self,
                    device      = '/dev/void',
                    set_id      = True,
                    device_id   = "01",
                    debug       = True,
                 ):
        pass

    def add_message(self, message, page):
        print message, page

    def set_schedule(self, pages):
        print 'schedule:', pages

    def delete_pages(self):
        print 'delete pages'

    def end(self):
        pass

    def clear_screen(self):
        print 'clear screen'
