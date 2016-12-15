from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD,adam
from keras.models import load_model

import numpy as np

fin = open('test_new','r')

data = []

i = 0
for line in fin:
		data.append(line.strip().split(','))
fin.close()

#print data
data = np.array(data)

model = load_model('model')








result=model.predict(data)
result=np.array(result)
print result.shape

answer=np.zeros((606779))

for i in range(606779):
	tmp=result[i]
	answer[i]=tmp.argmax()





f=open('predict.csv','w');
f.write('id,label\n')
for i in range(606779):
        f.write('%d'%(i+1))
        f.write(',')
        f.write('%d'%(answer[i]))
        f.write('\n')

