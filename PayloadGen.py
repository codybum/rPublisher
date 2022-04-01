import random
import names
import uuid
import json

zipList = []
patientCode = ["0", "1"]

def init():
    zipcodesFile = 'kyzipdetails.csv'

    file1 = open(zipcodesFile, 'r')
    kyZipCodes = file1.readlines()

    count = 0
    # Strips the newline character
    for zipLine in kyZipCodes:
        # print(zipLine)
        if (count > 0):
            zipLine = zipLine.strip()
            zipSplit = zipLine.split(",")
            zipList.append(zipSplit[0])
        count = count + 1

    #for st in zipList:
    #    print(st)

def getrandpayload():
    #count = random.randint(1, 10)
    count = 1
    return getpayload(count)

def getpayload(count):

    patientList = []
    for i in range(count):
        patientList.append(getperson())

    return json.dumps(patientList)


def getperson():
    testing_id = random.randint(1, 10)
    first_name = names.get_first_name()
    #last_name = names.get_last_name()
    patient_name = names.get_first_name() + ' ' + names.get_last_name()
    patient_mrn = str(uuid.uuid1())
    patient_zipcode = random.choice(zipList)
    patient_status_code = random.choice(patientCode)

    patientRecord = dict()
    #patientRecord["first_name"] = first_name
    patientRecord["testing_id"] = testing_id
    patientRecord["patient_name"] = patient_name
    patientRecord["patient_mrn"] = patient_mrn
    patientRecord["patient_zipcode"] = patient_zipcode
    patientRecord["patient_status"] = patient_status_code
    patientRecord["contact_list"] = []
    contact_count = range(random.randint(1, 10))
    for n in contact_count:
        patientRecord["contact_list"].append(str(uuid.uuid1()))

    patientRecord["event_list"] = []
    event_count = range(random.randint(1, 5))
    for n in event_count:
        patientRecord["event_list"].append(str(uuid.uuid1()))

    return patientRecord
