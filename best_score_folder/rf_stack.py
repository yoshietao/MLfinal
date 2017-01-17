from sklearn import ensemble
import numpy as np

data  = []
ID  = [] 
fin = open('../divide_train','r')
i = 0
for line in fin:
	if i%2 ==0:
		data.append(line.strip().split(','))
	else:
		ID.append(line)
	i=i+1
data = np.array(data)
ID   = np.array(ID)
print data.shape, ID.shape
fin.close()
#---------------------------------------------
clf = ensemble.RandomForestClassifier()
clf = clf.fit(data,ID)
del data,ID
#---------------------------------------------
fin = open('../divide_valid','r')
testdata = []
i = 0
for line in fin:
	if i%2 ==0:
		testdata.append(line.strip().split(','))
	i = i+1
fin.close()
testdata = np.array(testdata)
print testdata

x = clf.predict(testdata)
print x.shape
del testdata
#----------------------------------------------

fout = open('../data/stack_rf_valid.csv','w')
fout.write('id,label\n')
for i in range(496465):
	fout.write(str(i+1)+','+str(x[i]))
#--------------------------------------------------------------
fin = open('../../1ofnencoding/test-1ofn','r')
testdata = []
for line in fin:
	testdata.append(line.strip().split(','))
fin.close()
testdata = np.array(testdata)

x = clf.predict(testdata)
print x.shape
del testdata
#----------------------------------------------

fout = open('../data/stack_rf_test.csv','w')
fout.write('id,label\n')
for i in range(606779):
        fout.write(str(i+1)+','+str(x[i]))