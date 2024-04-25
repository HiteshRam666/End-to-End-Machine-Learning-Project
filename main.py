import os
import sys
from sensor.exception import SensorException
from sensor.logger import logging

def test_exception():
    try:
        logging.info("Zero division error will occur")
        a = 1/0
    except Exception as e:
        raise SensorException(e, sys)

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e) 