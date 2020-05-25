#Program to read the values of Temp and Hum from the DHT11 sensor and send it over to AWS-IOT

#Website: www.circuitdigest.com
import serial
import sys
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient #Import from AWS-IoT Library
import time#To create delay
from datetime import date, datetime #To get date and time

myMQTTClient = AWSIoTMQTTClient("$aws/things/Farm2/shadow/update")
myMQTTClient.configureEndpoint("aaf057clm4vjd-ats.iot.us-east-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("/home/pi/Downloads/aws-iot-device-sdk-python/<AMAZON_ROOT_CA>", "/home/pi/Downloads/aws-iot-device-sdk-python/<DEVICE_PRIVATE_KEY>", "/home/pi/Downloads/aws-iot-device-sdk-python/<DEVICE_CERTIFICATE>")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec


port = "/dev/ttyACM0"
s1 = serial.Serial(port,9600)
s1.flushInput()

connecting_time = time.time() + 10

if time.time() < connecting_time:  #try connecting to AWS for 10 seconds
    myMQTTClient.connect()
    myMQTTClient.publish("iot/info", "connected", 0)
    print ("MQTT Client connection success!")
    while 1: #Infinite Loop
        now = datetime.utcnow() #get date and time 
        current_time = now.strftime('%Y-%m-%dT%H:%M:%SZ') #get current time in string format 
    
        ph = s1.read(5).decode('utf-8')
        Temp = s1.read(5).decode('utf-8')
        humid = s1.read(5).decode('utf-8')

    #prepare the payload in string format 
        payload = '{ "timestamp": "' + current_time + ',"Ph": '+str(ph)+' ,"temperature": ' + str(Temp) + ',"humidity": '+ str(humid) + ' }'

        print (payload) #print payload for reference 
        myMQTTClient.publish("iot/data", payload, 0) #publish the payload
        time.sleep(2) #Wait for 2 sec then update the values
    
else:
    print ("Error: Check your AWS details in the program")

    



myMQTTClient.disconnect()