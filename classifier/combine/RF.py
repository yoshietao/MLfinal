
from sklearn.ensemble import RandomForestClassifier
import numpy as np

c1=np.loadtxt('../test/predict_class1.csv',delimiter=',')
c3=np.loadtxt('../test3/predict_class3.csv',delimiter=',')
c4=np.loadtxt('../test4/predict_class4.csv',delimiter=',')


c=np.column_stack((c1,c3,c4))

print c.shape


x=np.zeros([606779,1])
for i in range(606779):
	x[i]=np.max(c[i]).astype(int)




f=open('predict_classifier.csv','w');
f.write('id,label\n')
for i in range(606779):
	f.write('%d'%(i+1))
	f.write(',')
	f.write('%d'%(x[i]))
	f.write('\n')



