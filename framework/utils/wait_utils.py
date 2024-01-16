import logging
import time


class WaitUtils:
    @staticmethod
    def sleep(sec):
        logging.info(f"Sleep for {sec}s")
        return time.sleep(sec)
