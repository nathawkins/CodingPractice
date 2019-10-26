#include <iostream>
#include <math.h>
using namespace std;

int pentN(int n){
    return n*(3*n-1)/2;
}

int* generalizedPentNumbers(int* g, int num){
    g[0] = 0;
    int ind = 1;
    for(int i = 1; i <= num/2; i++){
        g[ind] = pentN(i);
        ind++;
        g[ind] = pentN(-1*i);
        ind++;
    }
    return g;
}

long pN(long n, int* gk, int start, int len){
    long sum = 0;

    if(n <= 1)
        return 1;

    long term;
    for(int k = start; k < len; k++){
        if ((n - gk[k]) < 0){
            cout << n << ", " << sum << ", " << k << endl;
            return sum;
        }
        term = pow(-1, k) * pN(n - gk[k], gk, start + 1, len);
        sum += term;
        sum %= 1000000;
    }
    return sum;
}

int main(int argc, char* argv[]){
    int arr[500];
    int* g = generalizedPentNumbers(arr, 500);
    cout << pN(5, g, 0, 500) << endl;
    return 0;
}