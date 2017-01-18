
from sklearn.ensemble import RandomForestClassifier
import numpy as np

"""
print "ID"
ID=np.loadtxt('newID',delimiter=',')

print "data"
data=np.loadtxt('data',delimiter=',')


print "testdata"
testdata=np.loadtxt('test-1ofn',delimiter=',')


for time in range(100):

	print time

	clf = RandomForestClassifier(n_estimators=10,class_weight={0:0.2333,1:1.8712})
	classifier = clf.fit(data,ID)


	print "predict"
	predictions = classifier.predict_proba(testdata)

	np.savetxt('pree'+str(time),predictions,delimiter=',')




"""

num=30
mat=np.zeros([606779,num])
matt=np.zeros([606779,1])

for number in range(num):
	predictions=np.loadtxt('pree'+str(number),delimiter=',')

	k=0	
	for i in range(606779):
		if predictions[i][1] >0:
			mat[i][number]=1
			matt[i][0]=1
			k=k+1
		else:
			mat[i][number]=0;
	print k



mat.astype(int)
print mat



"""
x=np.zeros([606779,1])

for i in range(606779):
	count=np.bincount(mat[i].astype(int))
	x[i]=np.argmax(count)

"""


f=open('predict_class1.csv','w');
for i in range(606779):
	f.write('%d'%(matt[i]))
	f.write('\n')



