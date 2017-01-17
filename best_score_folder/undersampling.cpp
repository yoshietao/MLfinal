#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <cstring>
#include <vector>
using namespace std;

/*
class0: 734536
class1: 230990
class2: 43
class3: 902
class4: 12757
*/

void savefile(int , istream *, ostream *);

int main()
{
	ifstream ifs("../1ofnencoding/train-1ofn-back");

	ofstream ofs("divide_train");
	savefile(0,&ifs, &ofs);
	ifs.close();
	ifstream ifs1("../1ofnencoding/train-1ofn-back");
	ofstream ofs1("divide_valid");
	savefile(1,&ifs1, &ofs1);
}


void savefile(int i, istream * ifs, ostream * ofs)
{
	string str;
	vector<int> count(2);
	while(getline(*ifs,str))
	{
		if(str.back() == '0')
		{
			count[0]++;
			if(count[0]%2 == i)  ///class 0 : 10000
			{
				*ofs<<str.substr(0,str.size()-2)<<endl;
				*ofs<<str.back()<<endl;
			}
		}
		else if(str.back() == '1') ///class 1 : 10000
		{
			count[1]++;
			if(count[1]%2 == i) 
			{
				*ofs<<str.substr(0,str.size()-2)<<endl;
				*ofs<<str.back()<<endl;
			}
		}
		else if(str.back() == '2') ///class 2 : 43*200
		{
			*ofs<<str.substr(0,str.size()-2)<<endl;
			*ofs<<str.back()<<endl;
		}
		else if(str.back() == '3') ///class 3 : 902*10
		{
			*ofs<<str.substr(0,str.size()-2)<<endl;
			*ofs<<str.back()<<endl;
		}
		else  //class 4 : 12757
		{ 
			*ofs<<str.substr(0,str.size()-2)<<endl;
			*ofs<<str.back()<<endl;
		}
	}
}