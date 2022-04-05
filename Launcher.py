import time

from PayloadGen import getpayload, init, getrandpayload
from Publisher import pub



init(100)

#payload = getpayload()
patient_list, hospital_list, vax_list = getpayload()


text_file = open("patient_data.json", "w")
n = text_file.write(patient_list)
text_file.close()

text_file = open("hospital_data.json", "w")
n = text_file.write(hospital_list)
text_file.close()

text_file = open("vax_data.json", "w")
n = text_file.write(vax_list)
text_file.close()


#with open('test_data.json', 'w') as f:
#    json.dump(payload, f, indent=4)

#while True:

    #payload = getrandpayload()
    #for x in range(1,17):
    #    pub(str(x),payload)
    #pub("patient_feed", payload)
    #time.sleep(2)