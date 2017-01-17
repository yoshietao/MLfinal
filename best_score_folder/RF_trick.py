
from sklearn.ensemble import RandomForestClassifier
import numpy as np

"""
print "ID"
ID=np.loadtxt('train_ID',delimiter=',')

print "data"
data=np.loadtxt('train_data',delimiter=',')


print "testdata"
testdata=np.loadtxt('test-1ofn',delimiter=',')
validdata=np.loadtxt('valid_data',delimiter=',')




for time in range(10):

	print time

	#clf = RandomForestClassifier(n_estimators=100,class_weight={0:0.2145,1:1.8712,2:5.3953,3:9.4989,4:0.6440})
	clf = RandomForestClassifier(n_estimators=100,class_weight={0:0.4290,1:3.7424,2:5.3953,3:9.4989,4:0.6440})
	classifier = clf.fit(data,ID)


	print "predict"
	predict_test = classifier.predict_proba(testdata)
	predict_valid= classifier.predict_proba(validdata)

	np.savetxt('predict_test_'+str(time),predict_test,delimiter=',')
	np.savetxt('predict_valid_'+str(time),predict_valid,delimiter=',')




"""

num=10


mat=np.zeros([606779,num])
matt=np.zeros([496465,num])

for number in range(num):
	print number
	predict_test=np.loadtxt('predict_test_'+str(number),delimiter=',')
	predict_valid=np.loadtxt('predict_valid_'+str(number),delimiter=',')





	for i in range(606779):
		if predict_test[i][3] >0:
			mat[i][number]=3
		elif predict_test[i][2] >=0.005:
			mat[i][number]=2
		elif predict_test[i][0] <=0.99:
			predict_test[i][0]=0
			mat[i][number]=np.argmax(predict_test[i])
		else:
			mat[i][number]=np.argmax(predict_test[i])




	for i in range(496465):
		if predict_valid[i][3] >0:
			matt[i][number]=3
		elif predict_valid[i][2] >=0.005:
			matt[i][number]=2
		elif predict_valid[i][0] <=0.99:
			predict_valid[i][0]=0
			matt[i][number]=np.argmax(predict_valid[i])
		else:
			matt[i][number]=np.argmax(predict_valid[i])


mat.astype(int)
matt.astype(int)


x=np.zeros([606779,1])
y=np.zeros([496465,1])


for i in range(606779):
	count=np.bincount(mat[i].astype(int))
	x[i]=np.argmax(count)



for i in range(496465):
	count=np.bincount(matt[i].astype(int))
	y[i]=np.argmax(count)


f=open('predict_test_1.csv','w');
f.write('id,label\n')
for i in range(606779):
	f.write('%d'%(i+1))
	f.write(',')
	f.write('%d'%(x[i]))
	f.write('\n')


f=open('predict_valid_1.csv','w');
f.write('id,label\n')
for i in range(496465):
	f.write('%d'%(i+1))
	f.write(',')
	f.write('%d'%(y[i]))
	f.write('\n')


