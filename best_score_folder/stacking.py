from sklearn.linear_model import LogisticRegression
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD,adam
from sklearn import tree
import numpy as np

#------------------------------------------------------
def readData(filename):
	x = [];
	ID = [];
	fin = open(filename,'r')
	i = 0
	for line in fin:
		if i>0:
			temp = np.array(line.strip().split(',')).astype('int')
			x.append(temp)
		i = i+1	
	x = np.array(x)
	print x.shape
	return x;
#------------------------------------------------------
def readY(filename):
	ID = [];
	fin = open(filename,'r')

	i = 0
	for line in fin:
		if i%2 ==1:
			ID.append(line)
		i=i+1
	ID   = np.array(ID)
	return ID;
#------------------------------------------------------
NN = readData('./csv/stack_NN_valid.csv')
RF = readData('./csv/stack_rf_valid.csv')
GTB = readData('./csv/stack_GTB_valid.csv')
DT = readData('./csv/stack_dt_valid.csv')
BEST = readData('./csv/stack_best_valid.csv')
BEST2 = readData('./csv/stack_best_valid_1.csv')
Y = readY('divide_valid').astype('int')

input4 = []
#print np.array([NN,RF,GTB,DT])
#.reshape(496465,20)
for i in range(496465):
	input4.append([NN[i].tolist(),RF[i].tolist(),GTB[i].tolist(),DT[i].tolist(),BEST[i].tolist(),BEST2[i].tolist()])
input4 = np.array(input4).reshape(496465,30)

#print input4,Y
#-----------------------------------------dt-----------------------------------------------------------------
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(input4,Y)
#print clf.score(input4,Y)
#-----------------------------------------NN----------------------------------------------------------

model = Sequential()
model.add(Dense(output_dim=10, input_dim=30))
model.add(Activation("relu"))
model.add(Dense(output_dim=5))
model.add(Activation("softmax"))

model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

model.fit(input4, Y, nb_epoch=5, batch_size=100)
score = model.evaluate(input4, Y)

#-----------------------logistic broken--------------------------------------------------------------------------------
'''
logistic = LogisticRegression(solver = 'sag', max_iter=100, random_state=42, multi_class = 'multinomial').fit(input4,Y)

print logistic.score(input4,Y)
'''
#----------------------------------------------------------------------------------------------------------------------
del NN,RF,GTB,DT,Y

NN1 = readData('./csv/stack_NN_test.csv').reshape(606779,5).astype('int')
RF1 = readData('./csv/stack_rf_test.csv').reshape(606779,5).astype('int')
GTB1 = readData('./csv/stack_GTB_test.csv').reshape(606779,5).astype('int')
DT1 = readData('./csv/stack_dt_test.csv').reshape(606779,5).astype('int')
BEST1 = readData('./csv/stack_best_test.csv').reshape(606779,5).astype('int')
BEST3 = readData('./csv/stack_best_test_1.csv').reshape(606779,5).astype('int')

test4 = []

for i in range(606779):
	test4.append([NN1[i].tolist(),RF1[i].tolist(),GTB1[i].tolist(),DT1[i].tolist(),BEST1[i].tolist(),BEST3[i].tolist()])
test4 = np.array(test4).reshape(606779,30)

result = np.array(model.predict(test4))
print result.shape

f = open('stacking_best1_temp2.csv','w')
f.write('id,label\n')
for i in range(606779):
	if (result[i].argmax()==0):
		if(result[i][0]<0.999):
			if(result[i][1]>result[i][3]):
				f.write(str(i+1)+','+str(1)+'\n')
			else:
				f.write(str(i+1)+','+str(3)+'\n')
		else:
			f.write(str(i+1)+','+str(0)+'\n')
	else:
		f.write(str(i+1)+','+str(result[i].argmax())+'\n')
