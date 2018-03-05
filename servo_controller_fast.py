from flask import Flask
from flask import jsonify
from time import sleep
from threading import Thread
import aiming_controller as ac
import os
app = Flask(__name__)
aiming = ac.AimingController(0.1, 0.2)

@app.route("/<numbers>", methods=["POST"])
def handle_numbers(numbers):
	result = {}
	
	try:
		int(numbers)
	except ValueError:
		result = {"result" : "invalid input"}
		return jsonify(result)
	
	if not check_valid_numbers(numbers):
		result = {"result" : "invalid set of numbers"}
		return jsonify(result)
	
	if aiming.is_busy():
		result = {"result" : "busy"}
		
	else:
		aiming.start_aiming(numbers)
		result = {"result" : "success"}
	
	return jsonify(result)
	
def check_valid_numbers(numbers):
	counter = 0
	for i in numbers:
		if int(i) == 8:
			counter += 1
	
	if counter >=3:
		return False
	else:
		return True
	
		
if __name__ == "__main__":
	app.run(host="0.0.0.0")

