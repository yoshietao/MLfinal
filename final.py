from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD,adam

import numpy as np

data = []
ID = [] 

for j in range (0):
	fin = open(str(j),'r')

	i = 0
	for line in fin:
		if i%2 ==0:
			data.append(line.strip().split(','))
		else:
			ID.append(line)	
		i=i+1
	fin.close()


'''

data=np.array(data)
ID=np.array(ID)

print data.shape
print ID.shape



model = Sequential()
model.add(Dense(output_dim=32, input_dim=41))
model.add(Activation("relu"))
model.add(Dense(output_dim=5))
model.add(Activation("softmax"))


model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

model.fit(data, ID, nb_epoch=5, batch_size=100)
score=model.evaluate(data,ID)
print('loss = ',score[0])
print('acc = ',score[1])



model.save('model')
'''