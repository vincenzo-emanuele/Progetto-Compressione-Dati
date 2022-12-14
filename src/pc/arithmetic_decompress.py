# 
# Decompression application using static arithmetic coding
#
# Usage: python arithmetic-decompress.py InputFile OutputFile
# This decompresses files generated by the arithmetic-compress.py application.
# 
# Copyright (c) Project Nayuki
# 
# https://www.nayuki.io/page/reference-arithmetic-coding
# https://github.com/nayuki/Reference-arithmetic-coding
# 

import sys
import pc.ae_lib.arithmeticcoding as arithmeticcoding


# Command line main application function.
def main(inputfile, outputfile):
	# Handle command line arguments
	'''if len(args) != 2:
		sys.exit("Usage: python arithmetic-decompress.py InputFile OutputFile")
	inputfile, outputfile = args'''
	
	# Perform file decompression
	with open(outputfile, "wb") as out, open(inputfile, "rb") as inp:
		bitin = arithmeticcoding.BitInputStream(inp)
		freqs = read_frequencies(bitin)
		decompress(freqs, bitin, out)


def read_frequencies(bitin):
	def read_int(n):
		result = 0
		for _ in range(n):
			result = (result << 1) | bitin.read_no_eof()  # Big endian
		return result
	
	freqs = [read_int(32) for _ in range(256)]
	freqs.append(1)  # EOF symbol
	return arithmeticcoding.SimpleFrequencyTable(freqs)


def decompress(freqs, bitin, out):
	dec = arithmeticcoding.ArithmeticDecoder(32, bitin)
	while True:
		symbol = dec.read(freqs)
		if symbol == 256:  # EOF symbol
			break
		out.write(bytes((symbol,)))


# Main launcher
'''if __name__ == "__main__":
	main(sys.argv[1 : ])
'''