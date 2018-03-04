import os

class LaserController:
		
	def export(self):
		try:
			os.system("echo 11 > /sys/class/gpio/export")
			os.system("echo out > /sys/class/gpio/gpio11/direction")
		except:
			pass
			
	def unexport(self):
		os.system("echo 11 > /sys/class/gpio/unexport")
		
	def turn_on(self):
		os.system("echo 1 > /sys/class/gpio/gpio11/value")
		
	def turn_off(self):
		os.system("echo 0 > /sys/class/gpio/gpio11/value")
