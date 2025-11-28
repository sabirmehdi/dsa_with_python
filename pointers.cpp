#include <iostream>
using namespace std;

struct Node
{
    int data= 10;
    string next ="0x00d123DECF4";
};

int main(){
    
  //Baisc access to value through pointer
    Node n1;
    Node *p;
    
    p=&n1; // one way of getting address of the location, other one is with key word 'new'.
    
    cout<<"Print with simple Struct method: ";
    cout<<n1.data<<endl;
    
    cout<<"Print with pointer 'p': ";
    cout<<(*p).data<<endl;

    cout<<"Print with (->) method: ";
    cout<<p->data<<endl;
    
    cout<<"Notice the data is value is changed now: ";
    (*p).data=20;
    cout<<(*p).data<<endl;
    
    
    // Creating new Node
    
    p= new Node;
    
    p->data= 30; // updating the data value of newly created node
    
    cout<<"This is address to new Node: "<<p<<endl; // prints the adress of new node
    
    cout<<"Data in New Node: "<<p->data<<endl; // prints the adress of new node
    
    
    // Deleting an existing instance
    
    // using "delete" key word to mark the memory as free for OS.
    
    delete p;
    
    cout<<p;
    
    

    
}