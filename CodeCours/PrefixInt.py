#!/usr/bin/env python3
""" @brief 	This program generates a prefix code for integers
"""

##############################################################################
# Algorithmic Information and Artificial Intelligence                        #
# http://teaching.simplicitytheory.science                Nils Holzenberger  #
# Telecom Paris  2024                                & jean-louis Dessalles  #
# -------------------------------------------------------------------------- #
##############################################################################

import sys
import os

___Correction = 1

def Binary(N):
	" returns the binary code of N as a string "
	return bin(N)[2:]	# bin(17) == '0b10001', so bin(17)[2:] == '10001'
	
def CrudeDoublingCode(N):
	""" returns a code in wich all bits in the binary representation of N are doubled, 
		and then the last bit is reversed
	"""
	Double = ''.join([b * 2 for b in Binary(N)])	
	return Double[:-1] + str((1 - int(Double[-1])))

def DoublingLengthCode(N):
	" Returns a code in which the length of N is double-coded, followed by N in binary form "
	
	BN = Binary(N)
	#BN = CrudeDoublingCode(N)
	# vvvvvvvv  To be changed vvvvvvvv
	# Replace the return line below.
	# To do so, use the function CrudeDoublingCode to compute the string corresponding 
	# to the "doubling length code". 
	return CrudeDoublingCode(N)
	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def DoublingLengthDecode(BinN):
	" Interprets BinN as the double-length code of N "
	BinLength = ''	# binary reprentation of N's length
	BinN1 = iter(BinN)	# allows to loop over BinN's digits
	for B in BinN1:
		BinLength += B
		if next(BinN1) != B:	break	# consumes the next bit in BinN1
	Length = int(BinLength, 2)
	# vvvvvvvv  To be changed vvvvvvvv
	# fill in the '...' in the line below before uncommenting it
	# StrN = BinN[.... : ....]
	N = int(StrN, 2)
	return {'Number': N, 'Length': Length, 'Remainder': BinN[... : ...]}
	# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	

if __name__ == "__main__":	
	if len(sys.argv) == 2 and sys.argv[1].isdigit():
		N = int(sys.argv[1])
		PrefixCoded_N = DoublingLengthCode(N)
		print('Double-length coding for %d: %s' % (N, PrefixCoded_N))
		print('Decoding %s: %s' % (PrefixCoded_N, DoublingLengthDecode(PrefixCoded_N)))
	else:
		print("\tUsage: %s <int>" % os.path.basename(sys.argv[0]))
		print(__doc__)
	
__author__ = 'Dessalles'
