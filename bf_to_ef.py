#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
	print('Needs a file to convert')
	sys.exit(-1)

with open(sys.argv[1], 'r') as f:
	data = f.read()


out = "skr"
chrs = {
	"+": "eee",
	"-": "eeE",
	"<": "eEe",
	">": "eEE",
	"[": "Eee",
	"]": "EeE",
	".": "EEe",
	",": "EEE",
}
for d in data:
	if d in chrs:
		out += chrs[d]
print(out)
