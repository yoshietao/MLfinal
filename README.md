# MLfinal
	In train	original-->delete same data
	normal		875363-->734536
	----------------------------
	back 		1971-->884
	teardrop 	881-->834
	smurf 		2527107-->2771
	land 		19-->17
	neptune 	964959-->226289
	pod 		244-->195
	-----------------------------
	buffer_overflow 25
	perl 		1
	rootkit 	8
	loadmodule 	9	
	----------------------------
	ftp_write 	8
	guess_passwd 	47
	imap 		980-->12
	spy 		1
	warezclient 	914-->805
	warezmaster 	18
	multihop 	7
	phf 		4
	----------------------------
	nmap 		2080-->1369
	ipsweep 	11272-->3469
	portsweep 	9328-->3256
	satan 		14309-->4636
### yoshie
#### after deleting same data:	
	class0: 734536
	class1: 230990
	class2: 43
	class3: 902
	class4: 12757
#### up to now, 0.95 kaggle performance with 1 NN layer, and 1 softmax layer. 

### changhc
####cyber.py
	ver 1:
	score = 0.95682 using 2 layers (32, 32) (relu, relu) and 1 softmax output.

##TODO
* Deal with unbalanced training set
	* https://www.quora.com/In-classification-how-do-you-handle-an-unbalanced-training-set
	* http://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/
