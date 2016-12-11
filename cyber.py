from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn import svm
from sklearn.cluster import KMeans, MiniBatchKMeans
from keras.layers import Input, Dense, Activation
from keras.models import Model
from keras.optimizers import Adam, SGD;
import time, csv, pandas, numpy
from keras.models import Sequential

protocol_type = {'tcp': 0, 'udp': 1, 'icmp': 2};
services = {'netbios_dmg': 0, 'tim': 1, 'urh': 2, 'ircu': 3, 'http_alt': 4, 'ntp': 5, 'aol': 6, 'auth': 7, 'snmp': 8, 'urp': 9, 'bgp': 10, 'courier': 11, 'csnet_ns': 12, 'ctf': 13, 'daytime': 14, 'discard': 15, 'domain': 16, 'domain_u': 17, 'echo': 18, 'eco': 19, 'eco_i': 20, 'ecr_i': 21, 'efs': 22, 'exec': 23, 'finger': 24, 'ftp': 25, 'ftp_data': 26, 'gopher': 27, 'harvest': 28, 'hostnames': 29, 'http': 30, 'http_2784': 31, 'http_443': 32, 'http_8001': 33, 'imap4': 34, 'IRC': 35, 'iso_tsap': 36, 'klogin': 37, 'kshell': 38, 'ldap': 39, 'link': 40, 'login': 41, 'mtp': 42, 'name': 43, 'netbios_dgm': 44, 'netbios_ns': 45, 'netbios_ssn': 46, 'netstat': 47, 'nnsp': 48, 'nntp': 49, 'ntp_u': 50, 'other': 51, 'pm_dump': 52, 'pop_2': 53, 'pop_3': 54, 'printer': 55, 'private': 56, 'red_i': 57, 'remote_job': 58, 'rje': 59, 'shell': 60, 'smtp': 61, 'sql_net': 62, 'ssh': 63, 'sunrpc': 64, 'supdup': 65, 'systat': 66, 'telnet': 67, 'tftp_u': 68, 'tim_i': 69, 'time': 70, 'urh_i': 71, 'urp_i': 72, 'uucp': 73, 'uucp_path': 74, 'vmnet': 75, 'whois': 76, 'X11': 77, 'Z39_50': 78, 'tcp': 79, 'icmp': 80};
flag = {'OTH': 0, 'REJ': 1, 'SHR': 2, 'RSTRH': 3, 'RSTO': 4, 'RSTOS0': 5, 'RSTR': 6, 'S0': 7, 'S1': 8, 'S2': 9, 'S3': 10, 'SF': 11, 'SH': 12};
attack_type = {'normal': 0, 'apache2': 1, 'back': 1, 'mailbomb': 1, 'processtable': 1, 'snmpgetattack': 1, 'teardrop': 1, 'smurf': 1, 'land': 1, 'neptune': 1, 'pod': 1, 'udpstorm': 1, 'ps': 2, 'buffer_overflow': 2, 'perl': 2, 'rootkit': 2, 'loadmodule': 2, 'xterm': 2, 'sqlattack': 2, 'httptunnel': 2, 'ftp_write': 3, 'guess_passwd': 3, 'snmpguess': 3, 'imap': 3, 'spy': 3, 'warezclient': 3, 'warezmaster': 3, 'multihop': 3, 'phf': 3, 'imap': 3, 'named': 3, 'sendmail': 3, 'xlock': 3, 'xsnoop': 3, 'worm': 3, 'nmap': 4, 'ipsweep': 4, 'portsweep': 4, 'satan': 4, 'mscan': 4, 'saint': 4, 'worm': 4};

def readData(filename, isTest):
	x = [];
	y = [];
	file = open(filename, 'r', encoding='utf-8');
	raw = csv.reader(file);
	for row in raw:
		temp = row;
		temp[1] = protocol_type[temp[1]];
		temp[2] = services[temp[2]];
		temp[3] = flag[temp[3]];
		if(not isTest):
			y.append(attack_type[temp[len(temp) - 1].replace('.', '')]);
			temp.remove(temp[len(temp) - 1]);
		temp = [float(i) for i in temp];
		x.append(temp);
	file.close();
	if(not isTest):
		return x, y;
	else:
		return x;

def write_result(filename, result_label):
	file = open(filename, 'w');
	file.write("id,label\n");
	for i in range(0, len(result_label)):
		file.write(str(i + 1) + "," + str(result_label[i]) + "\n");
	file.close();

def main():
	test_x = readData('./data/test.in', True);
	x, y = readData('./data/train', False);

	model = Sequential()
	model.add(Dense(output_dim=32, input_dim=41))
	model.add(Activation("relu"))
	model.add(Dense(32))
	model.add(Activation("relu"))
	model.add(Dense(output_dim=5))
	model.add(Activation("softmax"))
	model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])
	model.fit(x, y, nb_epoch=10, batch_size=1000, verbose=1, validation_split=0.05, shuffle=True);
	result = model.predict(test_x, verbose=1);
	result_label = numpy.argmax(result, axis = 1);

	write_result('./predict.csv', result_label);

if __name__ == '__main__':
	main()