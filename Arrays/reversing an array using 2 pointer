#include<iostream>
using namespace std;
int main(){
    int arr[5];
    for(int i=0; i<5;i++){
        cout<<"Enter the element"<<" "<<i+1<<endl;
        cin>>arr[i];
    }
    int i=0;
    int j=4;
    // I have taken this condition because it is an array with odd no. of elements
    while(i<j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
        i++; 
        j--;
        //these ++ and -- are done so that we can move towards the centre
        //as j starts from the end of the array whereas i starts from the beginning of the array

    }
    // now I will print the reversed array
    for(int i=0;i<5;i++){
        cout<<arr[i]<<" ";

    }
    return 0;
}
