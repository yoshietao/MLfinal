# MLfinal
### yoshie
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
#### after deleting same data:	
	class0: 734536
	class1: 230990
	class2: 43
	class3: 902
	class4: 12757
#### up to now, 0.95 kaggle performance with 1 NN layer, and 1 softmax layer. 
#### compare test and train set 
	I found that 419773 out of 606799 records in the test set can be found in train set.
	Thus We can check if we predict correctly on these records, and can modify the incorrect ones. 
### changhc
####cyber.py
######ver 1:
	score = 0.95682 using 2 layers (32, 32) (relu, relu) and 1 softmax output.  --> weak baseline passed
	
######ver 2:
	use SMOTE regular to oversample class 2 and 3
		exp 1: remove duplicate, SMOTE once
			false batch size but I'm not submitting this again now.
		exp 2: no removal
			0.95592, batch size = 1000 and shouldn't be too high
		exp 3: remove duplicate, SMOTE until all classes have the same amount of data
			0.95776, improved but still far from strong baseline.

##TODO
* Deal with unbalanced training set
	* https://www.quora.com/In-classification-how-do-you-handle-an-unbalanced-training-set
	* http://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/
* According to this site, class R2L may have more data in the testing set than we imagined, so this can be something that we should tackle.
	* http://cseweb.ucsd.edu/~elkan/clresults.html
*SMOTE toolkit
	*http://contrib.scikit-learn.org/imbalanced-learn/generated/imblearn.over_sampling.SMOTE.html
