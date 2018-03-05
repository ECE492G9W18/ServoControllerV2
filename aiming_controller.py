from threading import Thread, Lock
from time import sleep
import laser_controller as l
import os
import operator

class AimingController:
	def __init__(self):
		self.min_X = 138
		self.mid_X = 120
		self.max_X = 110

		self.min_Y = 72
		self.mid_Y = 82
		self.max_Y = 88
		
		self.calib_X = 120
		self.calib_Y = 100
		
		self.busy = False
		self.busy_mutex = Lock()
		
		self.delay_time = 0.8
		
		self.horizontal_dirs = [
			self.min_X, self.mid_X, self.max_X,  
			self.min_X, self.mid_X, self.max_X, 
			self.min_X, self.mid_X, self.max_X,
			self.calib_X]
		
		self.vertical_dirs = [
			self.max_Y, self.max_Y, self.max_Y, 
			self.mid_Y, self.mid_Y, self.mid_Y, 
			self.min_Y, self.min_Y, self.min_Y,
			self.calib_Y]
			
		self.laser = l.LaserController()
		self.laser_port = 11
	
	def aim_blocks(self, input_numbers):
		
		self.set_busy(True)
		self.laser.export(self.laser_port)
		self.laser.turn_on()
		
		seen = set()
		
		mapped_numbers = self.map_numbers(input_numbers)
		print(mapped_numbers)
		
		for i in mapped_numbers:
			if int(i) not in seen:
				# print(i)
				seen.add(int(i))
				self.move_servo(int(i))

				sleep(0.1)
				self.laser.turn_on()				
				sleep(0.3)
				
				self.laser.turn_off()
				self.move_servo(len(self.horizontal_dirs))
				
				
		if len(seen) != 9:
			i = 1
			while (i < 10):
				if i not in seen:
					print(i)
					seen.add(i)
					self.move_servo(int(i))
				i += 1
							
		self.laser.turn_off()
		self.laser.unexport(self.laser_port)
		sleep(5)
		self.set_busy(False)
		
	def map_numbers(self, input_numbers):
		mapping = {}
		
		i = 1
		for curr in input_numbers:
			mapping[i] = int(curr)
			i += 1
		
		ordered_mapping = sorted(mapping.items(), key=operator.itemgetter(1))
		
		return [x[0] for x in ordered_mapping]
		
	def start_aiming(self, numbers):
		thread = Thread(target = self.aim_blocks, args=(numbers, ))
		thread.start()
				
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
