import os

class LaserController:
		
	def export(self, gpio_port):
		try:
			os.system("echo %i > /sys/class/gpio/export" % gpio_port)
			os.system("echo out > /sys/class/gpio/gpio11/direction")
		except:
			pass
			
	def unexport(self, gpio_port):
		os.system("echo %i > /sys/class/gpio/unexport" % gpio_port)
		
	def turn_on(self):
		os.system("echo 1 > /sys/class/gpio/gpio11/value")
		
	def turn_off(self):
		os.system("echo 0 > /sys/class/gpio/gpio11/value")
