import time

from PayloadGen import getpayload, init, getrandpayload
from Publisher import pub



init()

while True:

    payload = getrandpayload()
    for x in range(1,17):
        pub(str(x),payload)
    time.sleep(2)