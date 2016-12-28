from sklearn import tree
import numpy as np

fin = open('../test_new','r')
testdata = []
i = 0
for line in fin:
		testdata.append(line.strip().split(','))
fin.close()
testdata = np.array(testdata)
#---------------------------------------------
data  = []
ID  = [] 
fin = open('../train_new','r')
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


clf = tree.DecisionTreeClassifier()
clf = clf.fit(data,ID)

x = clf.predict(testdata)

print x.shape

fout = open('dt0.csv','w')
fout.write('id,label\n')
for i in range(606779):
        fout.write(str(i+1)+','+str(x[i]))