//
//  main.cpp
//  Sort_KNearSorted
//
//  Created by Xiangcao Liu on 8/3/15.
//  Copyright (c) 2015 Xiangcao Liu. All rights reserved.
//

#include <iostream>
#include <queue>
using namespace std;

//O(NK)
void insertionSort(int A[], int size){
    for(int i = 1; i < size; ++i){
        int k = i, key = A[i];
        for(int j = i-1; j >= 0; --j){
            if(A[j] > key){
                A[k] = A[j];
                cout<<"move"<<endl;
                k = j ;
            }
        }
        A[k] = key;
    }
}

//O(NLogK)
void sortKNearSortedUsingMinHeap(int A[], int size){
    
}
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    int A[] = {2,1,4,3,6,5};
    insertionSort(A, 6);
    for(int i = 0; i < 6; ++i){
        cout<< A[i] <<" ";
    }
    cout <<endl;
    return 0;
}
