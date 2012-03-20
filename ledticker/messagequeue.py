import time
import threading
import Queue

class MessageQueue:

    def __init__(self, transmitter, max_pages = 10, intervall = 15):

        self.max_pages = max_pages
        self.intervall = intervall
        self.transmitter = transmitter

        self._setup_thread()
   
    def _setup_thread(self):
        self.message_queue = Queue.Queue()
        self.running = True
        t = threading.Thread(target=self.message_loop)
        t.daemon = True
        t.start()

    def add_message(self, message):
        self.message_queue.put(message)

    def message_loop(self):
        next_page = 0
        full = False

        while self.running:

            message = self.message_queue.get()

            self.transmitter.add_message(message, next_page)
            self.transmitter.set_schedule([next_page])

            time.sleep(self.intervall)
            
            next_page += 1
            if next_page > self.max_pages:
                next_page = 0
                full = True

            schedule = range(0, self.max_pages)
            if not full:
                schedule = range(0, next_page)

            schedule.reverse()
            self.transmitter.set_schedule(schedule)
      
