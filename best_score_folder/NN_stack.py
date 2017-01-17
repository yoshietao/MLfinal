from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD,adam
from keras.callbacks import EarlyStopping
from keras.models import load_model
import numpy as np

data  = []
#data1 = []
ID  = [] 
#ID1 = []

fin = open('../divide_train','r')
i = 0
for line in fin:
	if i%2 ==0:
		data.append(line.strip().split(','))
	else:
		ID.append(line)	
	i=i+1
fin.close()
'''
fin = open('train_neww2','r')
i = 0
for line in fin:
	if i%2 ==0:
		data1.append(line.strip().split(','))
	else:
		ID1.append(line)	
	i=i+1
fin.close()
'''

data=np.array(data)
ID=np.array(ID)

print data.shape
print ID.shape


model = Sequential()
model.add(Dense(output_dim=32, input_dim=122))
model.add(Activation("relu"))
model.add(Dropout(0.25))
model.add(Dense(output_dim=10))
model.add(Activation("relu"))
model.add(Dropout(0.25))
model.add(Dense(output_dim=5))
model.add(Activation("softmax"))

model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

#earlystopping = EarlyStopping(monitor = 'val_loss', patience = 2)

model.fit(data, ID, nb_epoch=10, batch_size=100)#, callbacks=[earlystopping], validation_data=(data1,ID1))
#x = model.get_weights()
#del model
#-------------------------------------------------------------------------------------------------------
'''
model = load_model('emptymodel')
earlystopping = EarlyStopping(monitor = 'val_loss', patience = 2)
model.fit(data1, ID1, nb_epoch=20, batch_size=100, callbacks=[earlystopping], validation_data=(data,ID))
x1 = model.get_weights()
del model
'''
#-------------------------------------------------------------------------------------------------------
#model = load_model('emptymodel')
'''
total_weight = []

for i in range(6):
	xx = (x[i]+x1[i])/2
	xx.astype('Float32')
	total_weight.append(xx)
#print total_weight

model.set_weights(total_weight)
score=model.evaluate(data,ID)
print('loss = ',score[0])
print('acc = ',score[1])
score=model.evaluate(data1,ID1)
print('loss = ',score[0])
print('acc = ',score[1])

model.save('model32105')
'''
fin = open('../divide_valid','r')
testdata = []
i = 0
for line in fin:
	if i%2 ==0:
		testdata.append(line.strip().split(','))
	i = i+1
fin.close()
testdata = np.array(testdata)

result=model.predict(testdata)
result=np.array(result)
print result.shape

answer=np.zeros((496465))

for i in range(496465):
	tmp=result[i]
	answer[i]=tmp.argmax()

f=open('../data/stack_NN_valid.csv','w');
f.write('id,label\n')
for i in range(489615):
	f.write('%d'%(i+1))
	f.write(',')
	f.write('%d'%(answer[i]))
	f.write('\n')
#-----------------------------------------------
fin = open('../../1ofnencoding/test-1ofn','r')
testdata = []
for line in fin:
	testdata.append(line.strip().split(','))
fin.close()
testdata = np.array(testdata)

result=model.predict(testdata)
result=np.array(result)
print result.shape

answer=np.zeros((606779))

for i in range(606779):
	tmp=result[i]
	answer[i]=tmp.argmax()

f=open('../data/stack_NN_test.csv','w');
f.write('id,label\n')
for i in range(606779):
        f.write('%d'%(i+1))
        f.write(',')
        f.write('%d'%(answer[i]))
        f.write('\n')