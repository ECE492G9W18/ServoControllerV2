from flask import Flask
from time import sleep

app = Flask(__name__)

min_X = 150
mid_X = 120
max_X = 100

min_Y = 90
mid_Y = 110
max_Y = 130

@app.route("/<numbers>", methods=["POST"])
def handle_numbers(numbers):
	for i in numbers:
		print(i)
		move_servo(int(i))
		sleep(0.2)

x = [min_X, mid_X, max_X, min_X, mid_X, max_X, min_X, mid_X, max_X]
y = [max_Y, max_Y, max_Y, mid_Y, mid_Y, mid_Y, min_Y, min_Y, min_Y]

def move_servo(block):
	with open("/dev/servoblaster", "w+") as fd:
		fd.write("0=%i\n" % x[block-1])
		fd.write("1=%i\n" % y[block-1])
		
		
		
if __name__ == "__main__":
	app.run(host="0.0.0.0")

