import numpy as np
import sys

ifile = sys.argv[1]
ofile = sys.argv[2]
num   = sys.argv[3]

#------------------------------------------------------
def readData(filename):
	x = [];
	ID = [];
	fin = open(filename,'r')

	for line in fin:
		x.append(line.strip().split(','))
	x = np.array(x)
	print x.shape 
	ID = x[1:,1:]
	return ID;
#------------------------------------------------------

NN = readData(ifile).reshape(int(num),).astype('int')

f = open(ofile,'w')

f.write('id,label\n')

for i in range(int(num)):
	if NN[i] == 0:
		f.write('1,0,0,0,0\n')
	if NN[i] == 1:
		f.write('0,1,0,0,0\n')
	if NN[i] == 2:
		f.write('0,0,1,0,0\n')
	if NN[i] == 3:
		f.write('0,0,0,1,0\n')
	if NN[i] == 4:
		f.write('0,0,0,0,1\n')	