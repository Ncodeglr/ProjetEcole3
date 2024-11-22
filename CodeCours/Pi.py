#!/usr/bin/env python3
""" @brief 
Computes pi (a concise, though quite inefficient, program) 
"""


##############################################################################
# Algorithmic Information and Artificial Intelligence                        #
# http://teaching.simplicitytheory.science                Nils Holzenberger  #
# Telecom Paris  2024                                & jean-louis Dessalles  #
# -------------------------------------------------------------------------- #
##############################################################################
import sys
import os
import math

def usage():	return """
Usage: %s <iterations>	
	--> prints pi based on <iterations> terms of the series
""" % os.path.basename(sys.argv[0])

def pi(N):
	PiDividedByFour = 0
	for i in range(N):
		PiDividedByFour += (-1)**i / float(2*i+1)
	return 4* PiDividedByFour
	
if __name__ == "__main__":
	print(__doc__)
	if len(sys.argv) > 1:	
		Arg = 0
		try:	Arg = int(sys.argv[1])
		except ValueError:	print('Please input positive integer')
		if Arg > 0:
			print("Approximation for %d terms:\n\t%12.10f\npython's value:\n\t%12.10f" % (Arg, pi(Arg), math.pi))
	else:
		print(usage())
		print('Example: pi(%d) = %f' % (100, pi(100)))

	
__author__ = 'Dessalles'
