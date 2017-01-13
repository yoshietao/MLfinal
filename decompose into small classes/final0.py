from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD,adam
from keras.callbacks import EarlyStopping
from keras.models import load_model
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
fin = open('train_new0','r')
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
model.add(Dense(output_dim=32))
model.add(Activation("relu"))
model.add(Dropout(0.25))
model.add(Dense(output_dim=23))
model.add(Activation("softmax"))

model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])
earlystopping = EarlyStopping(monitor = 'val_acc', patience = 2)
model.fit(data, ID, nb_epoch=5, batch_size=100)#, callbacks=[earlystopping], validation_data=(data1,ID1))
score=model.evaluate(data,ID)
print('loss = ',score[0])
print('acc = ',score[1])

predict = model.predict(testdata)
predict = np.argmax(predict,axis = 1)

fout = open('attacktype.csv','w')
fout.write('id,label\n')
for i in range(606779):
	if predict[i] == 12:
		fout.write(str(i+1)+','+str(0)+'\n')
	elif predict[i] in ([1,7,10,15,19,21]):
		fout.write(str(i+1)+','+str(1)+'\n')
	elif predict[i] in ([2,8,13,17]):
		fout.write(str(i+1)+','+str(2)+'\n')
	elif predict[i] in ([0,3,4,5,9,14,20,22]):
		fout.write(str(i+1)+','+str(3)+'\n')
	elif predict[i] in ([6,11,16,18]):
		fout.write(str(i+1)+','+str(4)+'\n')