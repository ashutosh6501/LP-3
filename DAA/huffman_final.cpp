#include<iostream>
#include<queue>  //string is stored in queue
#include<string>
using namespace std;
struct node{
	char data;
	int freq;
	const node *child0,*child1;
	
	node(char d,int f){
		data = d;
		freq = f;
		child0 = NULL;
		child1 = NULL;
		
	}
	
	node(const node *c0,const node *c1){
		data = 0;
		freq = c0->freq + c1->freq;  //pointer get value from line 57 & 60
		child0 = c0;
		child1 = c1;
	}
	
	bool operator<(const node &a)const{  //< operator will find out priority in queue which is min and max
	    return freq > a.freq;
	}
	
	void traverse(string code=" ")const{
		if(child0!=NULL){
			child0->traverse(code+'0');
			child1->traverse(code+'1');
		}
		else{
			cout<<"data: "<<data<<", freq: "<<freq<<", code: "<<code<<endl;
		}
	}
};
void huffmanCoding(string str){
	priority_queue<node> qu; //qu is object
	int frequency[256] = {0};  //set all frequencies as 0
	
	for(int i=0;i<str.size();i++){
		
			frequency[int(str[i])]++;  //as we traverse through string frequency will be increased in the list created in which character and its frequency will be stored
		
	}
	for(int i=0;i<256;i++){
		
		if(frequency[i]!=0){
			qu.push(node(i,frequency[i]));  //data and frequency will be stored priority wise
		}
		
		
	}
	while(qu.size()>1){ //until qu gets empty
		node *c0 = new node(qu.top()); //get left child and remove from queue
		qu.pop();
		
		node *c1 = new node(qu.top()); //get right child and remove from queue
		qu.pop();
		
		qu.push(node(c0,c1)); //add frequency of two child and push in queue
	}
	
	qu.top().traverse();  //traverse the tree to get the code
	cout<<"huffman code is: "<<endl;
}
int main(){
	string str = "AABBBBBBACADDDDBB";
	huffmanCoding(str);
	return 0;
}
