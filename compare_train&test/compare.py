import numpy as np

def readData(filename):
	data = [];
	fin = open(filename,'r')
	for line in fin:
		data.append(line.strip().split(','))
	data = np.array(data)
	fin.close();
	return data;
#--------------------------------------------
data   = readData('testlimit20+20.csv')
data1 = readData('predict_dt_noremoval.csv')

#print data[3][0]
#print data1[int(data[3][0])][1], data[3][1]
count = 0
for i in range (1,data.shape[0]):
	if data1[int(data[i][0])][1] != data[i][1]:
		count+=1
print count
