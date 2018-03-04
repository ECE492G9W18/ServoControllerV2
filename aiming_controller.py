from threading import Thread, Lock
from time import sleep
import laser_controller as l
import os

class AimingController:
	def __init__(self):
		self.min_X = 150
		self.mid_X = 120
		self.max_X = 100

		self.min_Y = 90
		self.mid_Y = 110
		self.max_Y = 130
		
		self.busy = False
		self.busy_mutex = Lock()
		
		self.delay_time = 0.2
		
		self.horizontal_dirs = [
			self.min_X, self.mid_X, self.max_X,  
			self.min_X, self.mid_X, self.max_X, 
			self.min_X, self.mid_X, self.max_X]
		
		self.vertical_dirs = [
			self.max_Y, self.max_Y, self.max_Y, 
			self.mid_Y, self.mid_Y, self.mid_Y, 
			self.min_Y, self.min_Y, self.min_Y]
			
		self.laser = l.LaserController()
	
	def aim_blocks(self, numbers):
		self.set_busy(True)
		self.laser.export()
		self.laser.turn_on()
		
		seen = set()
		
		for i in numbers:
			if int(i) not in seen:
				print(i)
				seen.add(int(i))
				self.move_servo(int(i))
				sleep(self.delay_time)
				
		if len(seen) != 9:
			i = 1
			while (i < 10):
				if i not in seen:
					print(i)
					seen.add(i)
					self.move_servo(int(i))
					sleep(self.delay_time)
				i += 1
							
		self.laser.turn_off()
		self.laser.unexport()
		
		self.set_busy(False)
		
	def start_aiming(self, numbers):
		print("starting aim")
		thread = Thread(target = self.aim_blocks, args=(numbers, ))
		thread.start()
		print("thread finished")
				
	def move_servo(self, block):
		with open("/dev/servoblaster", "w+") as fd:
			fd.write("0=%i\n" % self.horizontal_dirs[block-1])
			fd.write("1=%i\n" % self.vertical_dirs[block-1])
			
	def is_busy(self):
		self.busy_mutex.acquire()
		current_status = self.busy
		self.busy_mutex.release()
		return current_status
		
	def set_busy(self, busy_status):
		self.busy_mutex.acquire()
		self.busy = busy_status
		self.busy_mutex.release()
