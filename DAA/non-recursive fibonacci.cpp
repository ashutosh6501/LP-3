#include<iostream>
using namespace std;
int main(){
	int num,first=0,second=1,next;
	cout<<"Enter the terms of fibonacci series: "<<endl;
	cin>>num;
	
	int i=0;
	for(i=0;i<num;i++){
		cout<<first<<endl;
		next = first + second;
		first = second;
		second = next;
	}
	return 0;
}
