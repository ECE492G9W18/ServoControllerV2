from time import sleep
import os

if __name__ == "__main__":
	try:
		os.system("echo 11 > /sys/class/gpio/export")
		os.system("echo out > /sys/class/gpio/gpio11/direction")
	except:
		pass
		
	i = 0
	while(i < 10):
		os.system("echo 1 > /sys/class/gpio/gpio11/value")
		sleep(0.05)
		os.system("echo 0 > /sys/class/gpio/gpio11/value")
		sleep(0.5)
		i += 1
	
	os.system("echo 11 > /sys/class/gpio/unexport")
