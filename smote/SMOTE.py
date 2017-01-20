from sklearn import tree
from imblearn.over_sampling import SMOTE 
import numpy as np

data  = []
ID  = [] 
fin = open('../1ofnencoding/train-1ofn','r')
i = 0
for line in fin:
	if i%2 ==0:
		data.append(line.strip().split(','))
	else:
		ID.append(line)
	i=i+1
data = np.array(data)
data = data.astype('float32')
ID   = np.array(ID)
ID = ID.astype('float32')
print data.shape, ID.shape
fin.close()

smote = SMOTE()

X,Y = smote.fit_sample(data,ID)
print X.shape, Y.shape
del data,ID




clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
del X,Y

fin = open('../1ofnencoding/test-1ofn','r')
testdata = []
i = 0
for line in fin:
		testdata.append(line.strip().split(','))
fin.close()
testdata = np.array(testdata)
#---------------------------------------------

x = clf.predict(testdata)

del testdata

print x.shape


fout = open('dt_smote1.csv','w')
fout.write('id,label\n')
for i in range(606779):
        fout.write(str(i+1)+','+str(int(x[i]))+'\n')
