import time

from PayloadGen import getpayload, init, getrandpayload
from Publisher import pub



init()

import json

payload = getpayload()
print(payload)

text_file = open("test_data.json", "w")
n = text_file.write(payload)
text_file.close()

#with open('test_data.json', 'w') as f:
#    json.dump(payload, f, indent=4)

#while True:

    #payload = getrandpayload()
    #for x in range(1,17):
    #    pub(str(x),payload)
    #pub("patient_feed", payload)
    #time.sleep(2)