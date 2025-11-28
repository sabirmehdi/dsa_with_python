/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;

struct Node
{
    int data= 10;
    string next ="0x00d123DECF4";
};

int main(){
    
    Node n1;
    Node *p;
    
    p=&n1;
    
    cout<<"Print with simple Struct method: ";
    cout<<n1.data<<endl;
    
    cout<<"Print with pointer 'p': ";
    cout<<(*p).data<<endl;
    
    cout<<"Print with (->) method: ";
    cout<<p->data<<endl;
    
}