// Program to check if an array is sorted or not using non decreasing rule
#include<iostream>
using namespace std;
int main(){
    int arr[5];
    for(int i=0; i<5;i++){
        cout<<"Enter element"<<i+1<<": ";
        cin>>arr[i];
    }
    bool is_sorted=true;
    for(int i=0; i<4;i++){
        if(arr[i]>arr[i+1]){
            is_sorted=false;
            break;
        }
    }
    if(is_sorted)cout<<"Array is sorted in decreasing order";
    else cout<<"Array is not sorted";
    return 0;

}
