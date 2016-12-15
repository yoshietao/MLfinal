#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <cstring>
#include <vector>
#include <algorithm>
#include <ctime>
using namespace std;


int main()
{
	
	vector<string> data(979228);
	vector<char> id(979228);
	ifstream ifs("train_neww");
	string str;

	//srand (time(NULL));

	int counter = 0;
	while(getline(ifs,str))
	{
		//cout<<counter<<' ';
		data[counter]= str.substr(0,str.size()-2);
		id[counter]= str.back();
 		counter++;
 	}

	for(int i=0;i<4;i++)
	{
		int name=i;
		stringstream ss;
		ss<<name;
		string n=ss.str();

		ofstream ofs(n.c_str());
		for(int j=0;j<500000;j++)
		{
			int x = rand() % 979228;
			ofs<<data[x]<<endl;
			ofs<<id[x]<<endl;
		}
	}

	/*
	int div=1000000;
	for(int i=0;i<data.size();i=i+div)
	{
		int name=i/div;
		stringstream ss;
		ss<<name;
		string n=ss.str();

		ofstream ofs(n.c_str());
		int bound=min(i+div,int(data.size()));
		for(int j=i;j<bound;j++)
		{
			ofs<<data[j]<<endl;
			ofs<<id[j]<<endl;
		}
	}*/
/*
	int count=0;
	map<string, int>::iterator it;
	for(it = mm.begin() ; it != mm.end() ; it++)
		if(it->second==41)
		{
			cout<<"if(strcmp(token.c_str(),\""<<it->first<<"\""<<")==0) token=string(\""<<count<<"\");"<<endl;
			count++;
		}
*/
}

