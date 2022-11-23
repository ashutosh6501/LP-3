#include<iostream>
using namespace std;
bool issafe(int **arr,int x,int y,int n){
	for(int row=0;row<x;row++){  //checking for column
		if(arr[row][y] == 1){
			return false;
		}
	}
	
	int row =x;
	int col = y;
	
	while(row >= 0 && col>= 0 ){
		if(arr[row][col]==1){
			return false;
		}
		
		row--;
		col--;
	}
	
	row =x;
	col = y;
	
	while(row>= 0 && col<n ){
		if(arr[row][col]==1){
			return false;
		}
		
		row--;
		col++;
	}
	return true;
}

bool Nqueen(int** arr,int x,int n){  //no need to take column because as we place queen in a row no need to check further boxes in that row
	if(x>=n){  //we have placed n queens
		return true;
	}
	
	for(int col=0;col<n;col++){
		if(issafe(arr,x,col,n)){
			arr[x][col] =1;
			
			if(Nqueen(arr,x+1,n)){  //check for next row , RECURSION
				return true;
			}
			
			arr[x][col] = 0; //backtrack
		}
	}
	
	return false;
}
int main(){
	int n;
	cout<<"Enter no. of rows and columns"<<endl;
	cin>>n;
	
	int** arr = new int*[n];
	for(int i=0;i<n;i++){
		arr[i] = new int[n];
		for(int j=0;j<n;j++){
			arr[i][j] = 0;
		}
	}
	
	if (Nqueen(arr,0,n)){
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				cout<<arr[i][j]<<" ";
			}cout<<endl;
		}
		
	}
	return 0;
}
