#include<iostream>
using namespace std;
int first=0,second=1;

void recursion(int n){
	int next;
	if(n>0){
	
	next = first+second;
	first =second;
	second = next;
	cout<<next<<endl;
	recursion(n-1);
    }
}
int main(){
	int n;
	cout<<"enter number of terms"<<endl;
	cin>>n;
	cout<<"Fibonacci series: "<<endl;
	cout<<first<<endl;
	cout<<second<<endl;
	recursion(n-2);
	return 0;
}
