from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD,adam
from keras.callbacks import EarlyStopping
from keras.models import load_model
import numpy as np

data1 = []
ID1 = []
totalresult = []
result = np.zeros((606779,5))

fin = open('3','r')
i = 0
for line in fin:
	if i%2 ==0:
		data1.append(line.strip().split(','))
	else:
		ID1.append(line)	
	i=i+1
data1 = np.array(data1)
ID1   = np.array(ID1)
fin.close()

fin = open('test_new','r')
testdata = []

i = 0
for line in fin:
		testdata.append(line.strip().split(','))
fin.close()
testdata = np.array(testdata)

for x in range(3):
	data  = []
	ID  = [] 
	fin = open(str(x),'r')
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

	model = Sequential()
	model.add(Dense(output_dim=32, input_dim=41))
	model.add(Activation("relu"))
	model.add(Dropout(0.25))
	#model.add(Dense(output_dim=10))
	#model.add(Activation("relu"))
	#model.add(Dropout(0.25))
	model.add(Dense(output_dim=5))
	model.add(Activation("softmax"))

	model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])
	earlystopping = EarlyStopping(monitor = 'val_acc', patience = 2)
	model.fit(data, ID, nb_epoch=20, batch_size=100, callbacks=[earlystopping], validation_data=(data1,ID1))

	result = result + model.predict(testdata)
	#totalresult.append(result)

result/=3
print result

predict = np.argmax(result,axis = 1)

fout = open('predict1215-1.csv','w')
fout.write('id,label\n')
for i in range(606779):
        fout.write(str(i+1)+','+str(predict[i])+'\n')