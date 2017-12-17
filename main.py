print("[INFO] starting")

import machine, neopixel, time, sys
import uasyncio as asyncio
import urandom

# create a NeoPixel object
num_leds = 70
np1 = neopixel.NeoPixel(machine.Pin(2), num_leds)
np2 = neopixel.NeoPixel(machine.Pin(0), num_leds)

# https://learn.adafruit.com/led-tricks-gamma-correction/the-quick-fix
gamma = [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
          1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
          2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
          5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
         10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
         17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
         25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
         37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
         51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
         69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
         90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
        115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
        144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
        177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
        215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255 ]

def rainbow_rgb(minval, maxval, index, colors):
	max_index = len(colors)-1
	v = float(index-minval) / float(maxval-minval) * max_index
	i1, i2 = int(v), min(int(v)+1, max_index)
	(r1, g1, b1), (r2, g2, b2) = colors[i1], colors[i2]
	f = v - i1
	return gamma[int(r1 + f*(r2-r1))], gamma[int(g1 + f*(g2-g1))], gamma[int(b1 + f*(b2-b1))]
	


# FX switcher
current_fx = 1
async def switch_fx():
	global current_fx
	while True:
		current_fx = 1
		await asyncio.sleep(15)
		current_fx = 2
		await asyncio.sleep(15)

# base class
class neopixel_fx(object):
	def __init__(self, np, delay = 10):
		self.led_count = np.n
		self.delay = delay
		self.np = np
	def run(self):
		pass

# rainbow
class class_slide_rainbow(neopixel_fx):
	def __init__(self, np, delay = 10):
		super().__init__(np, delay)
		
		self.long_buf = bytearray(self.led_count*3)
		
		# fill array
		for i in range(self.led_count):
			# r, g, b  = rainbow_rgb(0, num_leds, i, [(64, 0, 0), (0, 0, 64), (0, 64, 0), (64, 0, 0)])
			r, g, b  = rainbow_rgb(0, num_leds, i, [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0)])
			offset = i * 3
			self.long_buf[offset + 0] = g
			self.long_buf[offset + 1] = r
			self.long_buf[offset + 2] = b
		
	async def run(self):
		global current_fx
		while True:
		# run 20 loops
		# for i in range(2):
			if current_fx == 1:
				for i in range(len(self.long_buf)//3):
					# [:3] is the list up to [3] and not including [3]
					# [3:] is the list from [3] to the end of the list
					self.long_buf = self.long_buf[3:] + self.long_buf[:3]
					self.np.buf = self.long_buf
					self.np.write()
					await asyncio.sleep_ms(self.delay)
				await asyncio.sleep(1)
				self.delay = urandom.getrandbits(4)
			else:
				await asyncio.sleep(1)

# falling stars
class class_falling2(neopixel_fx):
	def __init__(self, np, delay = 10):
		super().__init__(np, delay)
		self.star_length = 20
		star_buf = bytearray(self.star_length*3)
		# fill star array
		for i in range(self.star_length):
			r, g, b  = rainbow_rgb(0, self.star_length, i, [(255, 255, 255), (0, 0, 0)])
			offset = i * 3
			star_buf[offset + 0] = g
			star_buf[offset + 1] = r
			star_buf[offset + 2] = b
		# long array with hidden star
		self.long_buf = self.np.buf + star_buf
		
	async def run(self):
		global current_fx
		while True:
		# run 20 loops
		# for i in range(2):
			if current_fx == 2:
				print("cool 2")
				for i in range(len(self.long_buf)//3):
					# [:3] is the list up to [3] and not including [3]
					# [3:] is the list from [3] to the end of the list
					self.long_buf = self.long_buf[3:] + self.long_buf[:3]
					# self.np.buf = self.long_buf[self.star_length*3 : self.led_count*3 + self.star_length*3]
					self.np.buf = self.long_buf[0 : self.led_count*3]
					self.np.write()
					# time.sleep_ms(self.delay)
					await asyncio.sleep_ms(self.delay)
				await asyncio.sleep(0.2)
				self.delay = urandom.getrandbits(4)
			else:
				await asyncio.sleep(1)
			
my_falling1 = class_falling2(np1)
my_falling2 = class_falling2(np2)

my_slide_rainbow1 = class_slide_rainbow(np1)
my_slide_rainbow2 = class_slide_rainbow(np2)


loop = asyncio.get_event_loop()
loop.create_task( switch_fx() )
# fx 2
loop.create_task( my_falling1.run() )
loop.create_task( my_falling2.run() )
# fx 1
loop.create_task( my_slide_rainbow1.run() )
loop.create_task( my_slide_rainbow2.run() )

while True:
	loop.run_forever()

print("[INFO] finito")

