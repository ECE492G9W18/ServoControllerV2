from flask import Flask
from flask import jsonify
from time import sleep
from threading import Thread
import aiming_controller as ac
import os
app = Flask(__name__)
aiming = ac.AimingController()

delay_time = 0.2

@app.route("/<numbers>", methods=["POST"])
def handle_numbers(numbers):
	result = {}
	
	if aiming.is_busy():
		result = {"result" : "busy"}
		
	else:
		aiming.start_aiming(numbers)
		result = {"result" : "success"}
	
	return jsonify(result)
	
		
if __name__ == "__main__":
	app.run(host="0.0.0.0")

