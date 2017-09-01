import paho.mqtt.client as mqtt
import json
import os

#coding:utf-8
from socket import *
from time import ctime
import binascii
import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
########################
ENA = 13	#//L298A
ENB = 20	#//L298B
IN1 = 19	#1
IN2 = 16	#2
IN3 = 21	#3
IN4 = 26	#4
########################
IR_R = 18	#
IR_L = 27	#
########################
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
########################
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
ENA_pwm=GPIO.PWM(ENA,1000) #set initial frequency 
ENA_pwm.start(0)           #start pwm
ENA_pwm.ChangeDutyCycle(40) #change percentage
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
ENB_pwm=GPIO.PWM(ENB,1000) #set initial frequency 
ENB_pwm.start(0)           #start pwm
ENB_pwm.ChangeDutyCycle(40) #change percentage
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)

##################
GPIO.setup(IR_R,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(IR_L,GPIO.IN,pull_up_down=GPIO.PUD_UP)
##################

def ENA_Speed(EA_num):
	speed=hex(eval('0x'+EA_num))
	speed=int(speed,16) 
	print 'EA_A changed %d '%speed
	ENA_pwm.ChangeDutyCycle(speed)

def ENB_Speed(EB_num):
	speed=hex(eval('0x'+EB_num))
	speed=int(speed,16)
	print 'EB_B changed %d '%speed
	ENB_pwm.ChangeDutyCycle(speed)

def Motor_Forward():
	print 'motor forward'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)
def Motor_TurnLeft():
	print 'motor_turnleft'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)
def Motor_TurnRight():
	print 'motor_turnright'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)	
def Motor_Backward():
	print 'motor_backward'
	GPIO.output(ENA,True)
	GPIO.output(ENB,True)
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)
'''
###################################
##meet_black_turnright+back_or_turnleft+back_or_back
###################################
def	Avoiding():
	print IR_R
	time.sleep(1)
	if (GPIO.input(IR_R) == True) or (GPIO.input(IR_L) == True):
		if (GPIO.input(IR_L) == False):
			Motor_Backward()
			Motor_TurnLeft()
#			time.sleep(1)
			return
		else:
			Motor_Backward()
			Motor_TurnRight()
#			time.sleep(1)
			return
#		else ((GPIO.input(IR_R) == False)&( GPIO.input(IR_L) == False)):
	else:
		Motor_Forward()
		return

		if ((GPIO.input(IR_R) == False)&(GPIO.input(IR_L) == True)):
			Motor_Backward()
			time.sleep(2)
			return
		if ((GPIO.input(IR_R) == True)&(GPIO.input(IR_L) == True)):
			Motor_Backward()
			time.sleep(1)
			return


try:
	while True:
		Avoiding()#glud
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()

'''
###################################
##connection
###################################
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('mqtt')


def on_message(client, userdata, msg):
#    print  str(msg.payload)
#    print json.loads(msg.payload)
#    if msg.payload<5:
#        Motor_Backward()
#    else:
#        Motor_Forward()
    a = int(msg.payload)
    
def BackOrForward():
    if (on_message<=5)
        Motor_Backward()
        print 'back'
    else:
        Motor_Forward()
        print 'forward'

if __name__ == '__main__':
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	BackOrForward()
#####
	try:
		client.connect(host='10.16.89.91',port=1883,keepalive=60)
		client.loop_forever()
	except KeyboardInterrupt:
		client.disconnect()








