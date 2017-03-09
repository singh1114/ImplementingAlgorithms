#include <iostream>
using namespace std;
int top = -1;

/*
	The push function has three parameters
	First is the stack,
	second is the element that is needed to be added.
	third is the size of the stack.
*/
void push(int stack[], int x, int n) {
	if(top == n-1){
		cout<<"\nOverflow... There is no space in the stack";
	}
	else{
		top++;
		stack[top] = x; 
	}
}	

void pop(){
	if(top == -1){
		cout<<"\nnothing to delete";
	}
	else{
		top--;
	}
}

/*
	This function prints the size of the stack at a particular point
*/
void size() {
	cout<<"\nSize of the stack is : "<<top+1;
}


/*
	Now implement these functions in the main function.
*/
int main(){
	int stack[3];
	push(stack, 5, 3);

	size();

	push(stack, 4, 3);
	push(stack, -10, 3);
	for(int i=0; i<3;i++){
		cout<<"\n"<<stack[i];
	}

	// This will produce overflow
	push(stack, 10, 3);
	size();

	for(int i=0;i<3;i++){
		pop();
	}
	size();
	return 0;
}
