/*Write a program to perform linear search:
Take 5 integers in an array
Take an integer key to search
If the key is found:
print: Element found at index X
If not found:
print: Element not found*/
#include<iostream>
using namespace std;
int main(){
    int arr[5];
    for(int i=0;i<5;i++){
        cout<<"Enter element"<<i+1<<": ";
        cin>>arr[i];
    }
    int key;
    bool key_found=false;
    cout<<"Enter the number you want to search for: ";
    cin>>key;
    for(int i=0;i<5;i++){
        if(arr[i]==key){
            key_found=true;
            cout<<"Key found at index"<<i<<endl;
            break;
        }

    }
    
    if(key_found==false) cout<<"The key is not found";
    return 0;
}
