#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
	print('Needs a file to skree')
	sys.exit(-1)

with open(sys.argv[1], 'r') as f:
	data = f.read()

if data[0:3].lower() != 'skr':
	print('Skree needs to start with skr')
	sys.exit(-1)

counter = 3
band_position = 0
band = {}
def get_band(x):
	if not (x in band):
		band[x] = 0
	return band[x]
def inc_band():
	band[band_position] = get_band(band_position) + 1
def dec_band():
	band[band_position] = get_band(band_position) - 1
def set_band(x, n):
	get_band(x) # make sure it exists
	band[x] = int(n)
stack = []
while data[counter:counter+3]:
	skre = data[counter:counter+3]
	if skre.lower() != 'eee':
		counter += 1
		continue
	if skre == 'eee': # +
		inc_band()
	elif skre == 'eeE': # -
		dec_band()
	elif skre == 'eEe': # <
		band_position -= 1
	elif skre == 'eEE': # >
		band_position += 1
	elif skre == 'Eee': # [
		stack.append(counter)
	elif skre == 'EeE': # ]
		p = stack.pop()
		if get_band(band_position):
			# do the jump
			counter = p
			continue
	elif skre == 'EEe': # .
		print(chr(get_band(band_position)), end='')
	elif skre == 'EEE': # ,
		try:
			num = ord(sys.stdin.read(1))
		except:
			num = 0
		set_band(band_position, num)
	else:
		counter += 1
		continue
	
	counter += 3
