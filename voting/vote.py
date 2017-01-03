from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

#------------------------------------------------------
def readData(filename):
	x = [];
	#data = [];
	ID = [];
	fin = open(filename,'r')

	for line in fin:
		x.append(line.strip().split(','))
	x = np.array(x)
	print x.shape 
	#data = x[1:,:1]
	ID = x[1:,1:]
	return ID;
#-------------------------------------------------------
Y_dt1ofn = readData('dt_1hot.csv')
Y_GTB = readData('GTB.csv')
Y_dtno = readData('dt_noremoval.csv')
Y_vote = readData('vote.csv')
Y_gdbno = readData('gdb_noremoval.csv')

print Y_dt1ofn

fout = open('vote1.csv','w')
fout.write('id,label\n')
for i in range(606779):
	x = np.zeros(5)
	x[int(Y_dt1ofn[i][0])] = x[int(Y_dt1ofn[i][0])] + 1
	x[int(Y_GTB[i][0])] = x[int(Y_GTB[i][0])] + 1
	x[int(Y_dtno[i][0])] = x[int(Y_dtno[i][0])] + 1
	x[int(Y_vote[i][0])] = x[int(Y_vote[i][0])] + 1
	x[int(Y_gdbno[i][0])] = x[int(Y_gdbno[i][0])] + 1
	xmax = np.argmax(x)
	fout.write(str(i+1)+','+str(xmax)+'\n') 
   