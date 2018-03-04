import unittest
import aiming_controller

class TestServoController(unittest.TestCase):
	'''
	for block
		3 | 5 | 7
		1 | 4 | 9
		6 | 2 | 8
	
	it should return (4,8,1,5,2,7,3,9,6)
	'''
	
	def test_map_numbers(self):
		a = aiming_controller.AimingController()
		self.assertEqual(a.map_numbers("357149628"), [4,8,1,5,2,7,3,9,6])
		
if __name__ == "__main__":
	unittest.main()
		
