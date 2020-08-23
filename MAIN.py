import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
#Provide your IBM Watson Device Credentials
organization = "i8fmqf"
deviceType = "raspberry"
deviceId = "12345"
authMethod = "token"
authToken = "123456789"

'''
def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data['command'])

        if cmd.data['command']=='motoron':
                print("Motor ON IS RECEIVED")
                
                
        elif cmd.data['command']=='motoroff':
                print("MOTOR OFF IS RECEIVED")
'''        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        
        age=random.randint(0, 100)
        Temperature =random.randint(0, 100)
        Systolic =random.randint(0, 100)
        Diastolic =random.randint(0, 100)
        Pulse =random.randint(0, 100)
        #Send Temperature & Humidity to IBM Watson
        data = { 'age' : age, 'Temperature' : Temperature, 'Systolic':Systolic, 'Diastolic':Diastolic, 'Pulse':Pulse }
        #print (data)
        def myOnPublishCallback():
            print ("Published age = %s C" % age, "Temperature = %s %%" % Temperature, "Systolic = %s %%" % Systolic, "Diastolic = %s %%" % Diastolic, "Pulse = %s %%" % Pulse, "to IBM Watson")

        success = deviceCli.publishEvent("health", "json", data, qos=0, on_publish=myOnPublishCallback)
        if(Temperature<50):
                r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=q5lnG4atKdro1TQyMLiCgpFSJfVPBemw8uEkRWU9IAc3Y2Xxbhpwz6Nl0iu3bf9EoQJFW2C7VsMG4XID&sender_id=FSTSMS&message=Temperature is low... please switch on motor.&language=english&route=p&numbers=9611405758')
                print(r.status_code)
        if(Systolic<50):
                r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=q5lnG4atKdro1TQyMLiCgpFSJfVPBemw8uEkRWU9IAc3Y2Xxbhpwz6Nl0iu3bf9EoQJFW2C7VsMG4XID&sender_id=FSTSMS&message=Systolic is low... please switch on motor.&language=english&route=p&numbers=9611405758')
                print(r.status_code)
        if(Diastolic<50):
                r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=q5lnG4atKdro1TQyMLiCgpFSJfVPBemw8uEkRWU9IAc3Y2Xxbhpwz6Nl0iu3bf9EoQJFW2C7VsMG4XID&sender_id=FSTSMS&message=Diastolic is low... please switch on motor.&language=english&route=p&numbers=9611405758')
                print(r.status_code)
        if(Pulse<50):
                r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=q5lnG4atKdro1TQyMLiCgpFSJfVPBemw8uEkRWU9IAc3Y2Xxbhpwz6Nl0iu3bf9EoQJFW2C7VsMG4XID&sender_id=FSTSMS&message=Pulse is low... please switch on motor.&language=english&route=p&numbers=9611405758')
                print(r.status_code)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        #deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
