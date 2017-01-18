#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifs("ID");
	ofstream ofs("newID");

	string str;
	while(getline(ifs,str))
	{
		if(str.compare("4")==0)
			ofs<<"1"<<endl;
		else
			ofs<<"0"<<endl;
	}
}
