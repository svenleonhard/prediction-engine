import sys
import logging
import traceback
import threading
import multiprocessing
import time
from logging import FileHandler as FH


# ============================================================================
# Define Log Handler
# ============================================================================
class LogHandler(logging.Handler):
    """multiprocessing log handler

    This handler makes it possible for several processes
    to log to the same file by using a queue.

    """
    def __init__(self, fname):
        logging.Handler.__init__(self)

        self._handler = FH(self._make_filename(fname))
        self.queue = multiprocessing.Queue(-1)

        thrd = threading.Thread(target=self.receive)
        thrd.daemon = True
        thrd.start()

    @classmethod
    def _make_filename(self, fname):
        filename = []

        filename.append(fname)
        filename.append('_')

        unix_timestamp = int(time.time())
        filename.append(str(unix_timestamp))

        filename.append('.log')

        return ''.join(filename)

    def setFormatter(self, fmt):
        logging.Handler.setFormatter(self, fmt)
        self._handler.setFormatter(fmt)

    def receive(self):
        while True:
            try:
                record = self.queue.get()
                self._handler.emit(record)
            except (KeyboardInterrupt, SystemExit):
                raise
            except EOFError:
                break
            except Exception:
                traceback.print_exc(file=sys.stderr)

    def send(self, s):
        self.queue.put_nowait(s)

    def _format_record(self, record):
        if record.args:
            record.msg = record.msg % record.args
            record.args = None
        if record.exc_info:
            self.format(record)
            record.exc_info = None

        return record

    def emit(self, record):
        try:
            s = self._format_record(record)
            self.send(s)
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            self.handleError(record)

    def close(self):
        self._handler.close()
        logging.Handler.close(self)