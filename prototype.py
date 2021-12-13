import RPi.GPIO as GPIO
from flask import Flask
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(12, GPIO.OUT) 
GPIO.setup(16, GPIO.OUT)

app=Flask(__name__)

@app.route('/digital/write/forward')
def moveForward():
	GPIO.output(3, GPIO.HIGH)
	GPIO.output(12, GPIO.HIGH)
	return "Robot is moving forward!"

@app.route('/digital/write/backward')
def moveBackward():
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	return "Robot is moving backward!"

@app.route('/stop')
def stopRobot():
	GPIO.output(3, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	return "Robot has stopped moving."

@app.route('/digital/write/<pin_name>/<state>')
def digital_write(pin_name, state):
	pin_int = int(pin_name)
	state_int = int(state)
	if (pin_int == 3):
		if (state_int == 1):
			GPIO.output(3, GPIO.HIGH)
		elif (state_int == 0):
			GPIO.output(3, GPIO.LOW)
	elif (pin_int == 5):
		if (state_int == 1):
			GPIO.output(5, GPIO.HIGH)
		elif (state_int == 0):
			GPIO.output(5, GPIO.LOW)
	elif (pin_int == 12):
		if (state_int  == 1):
			GPIO.output(12, GPIO.HIGH)
		elif (state_int == 0):
			GPIO.output(12, GPIO.LOW)
	elif (pin_int == 16):
		if (state_int == 1):
			GPIO.output(16, GPIO.HIGH)
		elif (state_int == 0):
			GPIO.output(16, GPIO.LOW)
	return "Pin "+str(pin_int)+" is set to: "+str(state_int)

if (__name__ == "__main__"):
	app.run(debug=True, host='0.0.0.0')
