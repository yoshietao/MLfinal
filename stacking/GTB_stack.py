from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

data  = []
ID  = [] 
fin = open('../divide_all_train','r')
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

print '--start fit--'
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0).fit(data,ID)
del data,ID
print '--finish fit--'

fin = open('../divide_all_valid','r')
testdata = []
i = 0
for line in fin:
	if i%2 ==0:
		testdata.append(line.strip().split(','))
	i = i+1
fin.close()
testdata = np.array(testdata)

x = clf.predict(testdata)
del testdata
print '--finish predict--'

fout = open('../data/stack_all_GTB_valid.csv','w')
fout.write('id,label\n')
for i in range(489615):
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
fout = open('../data/stack_all_GTB_test.csv','w')
fout.write('id,label\n')
for i in range(606779):
        fout.write(str(i+1)+','+str(x[i]))