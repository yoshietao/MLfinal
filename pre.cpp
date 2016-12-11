#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <map>
#include <cstring>
#include <vector>
using namespace std;


int main()
{
	ifstream ifs("train");
	string str;
	map<string,bool> m;
	while(getline(ifs,str))
	{
		m[str]=true;
	}

	cout<<m.size()<<endl;

	vector<string> rawdata(m.size());
	int counter=0;
	map<string, bool>::iterator it;
        for(it = m.begin() ; it != m.end() ; it++)
	{
		rawdata[counter]=it->first;
		counter++;
	}
	

	ofstream ofs("train_new");
	
	for(int i=0;i<rawdata.size();i++)
	{
		istringstream ss(rawdata[i]);
		string token;

		int num=0;
		string newstr;
		while(getline(ss,token,','))
		{


if(num==1)
{
if(strcmp(token.c_str(),"icmp")==0) token=string("0");
if(strcmp(token.c_str(),"tcp")==0) token=string("1");
if(strcmp(token.c_str(),"udp")==0) token=string("2");
}

if(num==2)
{
if(strcmp(token.c_str(),"IRC")==0) token=string("0");
if(strcmp(token.c_str(),"X11")==0) token=string("1");
if(strcmp(token.c_str(),"Z39_50")==0) token=string("2");
if(strcmp(token.c_str(),"aol")==0) token=string("3");
if(strcmp(token.c_str(),"auth")==0) token=string("4");
if(strcmp(token.c_str(),"bgp")==0) token=string("5");
if(strcmp(token.c_str(),"courier")==0) token=string("6");
if(strcmp(token.c_str(),"csnet_ns")==0) token=string("7");
if(strcmp(token.c_str(),"ctf")==0) token=string("8");
if(strcmp(token.c_str(),"daytime")==0) token=string("9");
if(strcmp(token.c_str(),"discard")==0) token=string("10");
if(strcmp(token.c_str(),"domain")==0) token=string("11");
if(strcmp(token.c_str(),"domain_u")==0) token=string("12");
if(strcmp(token.c_str(),"echo")==0) token=string("13");
if(strcmp(token.c_str(),"eco_i")==0) token=string("14");
if(strcmp(token.c_str(),"ecr_i")==0) token=string("15");
if(strcmp(token.c_str(),"efs")==0) token=string("16");
if(strcmp(token.c_str(),"exec")==0) token=string("17");
if(strcmp(token.c_str(),"finger")==0) token=string("18");
if(strcmp(token.c_str(),"ftp")==0) token=string("19");
if(strcmp(token.c_str(),"ftp_data")==0) token=string("20");
if(strcmp(token.c_str(),"gopher")==0) token=string("21");
if(strcmp(token.c_str(),"harvest")==0) token=string("22");
if(strcmp(token.c_str(),"hostnames")==0) token=string("23");
if(strcmp(token.c_str(),"http")==0) token=string("24");
if(strcmp(token.c_str(),"http_2784")==0) token=string("25");
if(strcmp(token.c_str(),"http_443")==0) token=string("26");
if(strcmp(token.c_str(),"http_8001")==0) token=string("27");
if(strcmp(token.c_str(),"imap4")==0) token=string("28");
if(strcmp(token.c_str(),"iso_tsap")==0) token=string("29");
if(strcmp(token.c_str(),"klogin")==0) token=string("30");
if(strcmp(token.c_str(),"kshell")==0) token=string("31");
if(strcmp(token.c_str(),"ldap")==0) token=string("32");
if(strcmp(token.c_str(),"link")==0) token=string("33");
if(strcmp(token.c_str(),"login")==0) token=string("34");
if(strcmp(token.c_str(),"mtp")==0) token=string("35");
if(strcmp(token.c_str(),"name")==0) token=string("36");
if(strcmp(token.c_str(),"netbios_dgm")==0) token=string("37");
if(strcmp(token.c_str(),"netbios_ns")==0) token=string("38");
if(strcmp(token.c_str(),"netbios_ssn")==0) token=string("39");
if(strcmp(token.c_str(),"netstat")==0) token=string("40");
if(strcmp(token.c_str(),"nnsp")==0) token=string("41");
if(strcmp(token.c_str(),"nntp")==0) token=string("42");
if(strcmp(token.c_str(),"ntp_u")==0) token=string("43");
if(strcmp(token.c_str(),"other")==0) token=string("44");
if(strcmp(token.c_str(),"pm_dump")==0) token=string("45");
if(strcmp(token.c_str(),"pop_2")==0) token=string("46");
if(strcmp(token.c_str(),"pop_3")==0) token=string("47");
if(strcmp(token.c_str(),"printer")==0) token=string("48");
if(strcmp(token.c_str(),"private")==0) token=string("49");
if(strcmp(token.c_str(),"red_i")==0) token=string("50");
if(strcmp(token.c_str(),"remote_job")==0) token=string("51");
if(strcmp(token.c_str(),"rje")==0) token=string("52");
if(strcmp(token.c_str(),"shell")==0) token=string("53");
if(strcmp(token.c_str(),"smtp")==0) token=string("54");
if(strcmp(token.c_str(),"sql_net")==0) token=string("55");
if(strcmp(token.c_str(),"ssh")==0) token=string("56");
if(strcmp(token.c_str(),"sunrpc")==0) token=string("57");
if(strcmp(token.c_str(),"supdup")==0) token=string("58");
if(strcmp(token.c_str(),"systat")==0) token=string("59");
if(strcmp(token.c_str(),"telnet")==0) token=string("60");
if(strcmp(token.c_str(),"tftp_u")==0) token=string("61");
if(strcmp(token.c_str(),"tim_i")==0) token=string("62");
if(strcmp(token.c_str(),"time")==0) token=string("63");
if(strcmp(token.c_str(),"urh_i")==0) token=string("64");
if(strcmp(token.c_str(),"urp_i")==0) token=string("65");
if(strcmp(token.c_str(),"uucp")==0) token=string("66");
if(strcmp(token.c_str(),"uucp_path")==0) token=string("67");
if(strcmp(token.c_str(),"vmnet")==0) token=string("68");
if(strcmp(token.c_str(),"whois")==0) token=string("69");
}

if(num==3)
{
if(strcmp(token.c_str(),"OTH")==0) token=string("0");
if(strcmp(token.c_str(),"REJ")==0) token=string("1");
if(strcmp(token.c_str(),"RSTO")==0) token=string("2");
if(strcmp(token.c_str(),"RSTOS0")==0) token=string("3");
if(strcmp(token.c_str(),"RSTR")==0) token=string("4");
if(strcmp(token.c_str(),"S0")==0) token=string("5");
if(strcmp(token.c_str(),"S1")==0) token=string("6");
if(strcmp(token.c_str(),"S2")==0) token=string("7");
if(strcmp(token.c_str(),"S3")==0) token=string("8");
if(strcmp(token.c_str(),"SF")==0) token=string("9");
if(strcmp(token.c_str(),"SH")==0) token=string("10");
}


if(num==41)
{
if(strcmp(token.c_str(),"back.")==0) token=string("1");
if(strcmp(token.c_str(),"buffer_overflow.")==0) token=string("2");
if(strcmp(token.c_str(),"ftp_write.")==0) token=string("3");
if(strcmp(token.c_str(),"guess_passwd.")==0) token=string("3");
if(strcmp(token.c_str(),"imap.")==0) token=string("3");
if(strcmp(token.c_str(),"ipsweep.")==0) token=string("4");
if(strcmp(token.c_str(),"land.")==0) token=string("1");
if(strcmp(token.c_str(),"loadmodule.")==0) token=string("2");
if(strcmp(token.c_str(),"multihop.")==0) token=string("3");
if(strcmp(token.c_str(),"neptune.")==0) token=string("1");
if(strcmp(token.c_str(),"nmap.")==0) token=string("4");
if(strcmp(token.c_str(),"normal.")==0) token=string("0");
if(strcmp(token.c_str(),"perl.")==0) token=string("2");
if(strcmp(token.c_str(),"phf.")==0) token=string("3");
if(strcmp(token.c_str(),"pod.")==0) token=string("1");
if(strcmp(token.c_str(),"portsweep.")==0) token=string("4");
if(strcmp(token.c_str(),"rootkit.")==0) token=string("2");
if(strcmp(token.c_str(),"satan.")==0) token=string("4");
if(strcmp(token.c_str(),"smurf.")==0) token=string("1");
if(strcmp(token.c_str(),"spy.")==0) token=string("3");
if(strcmp(token.c_str(),"teardrop.")==0) token=string("1");
if(strcmp(token.c_str(),"warezclient.")==0) token=string("3");
if(strcmp(token.c_str(),"warezmaster.")==0) token=string("3");



}








if(num==41)
{
	ofs<<newstr.substr(0,newstr.size()-1)<<endl;
	ofs<<token<<endl;
}



newstr=newstr+token+',';
num++;

		}

 	}

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

