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

long* computePartitions(long* arr, long endpoint){
    arr[0] = 1;
    int coeff;
    int pent1;
    int pent2;
    for(long n = 1; n < endpoint; n++){
        for(int k = 1; k <= n; k++){
            coeff = pow(-1, k + 1);
            pent1 = pentN(k);
            pent2 = pentN(-1*k);

            if (n - pent1 >= 0){
                arr[n] += coeff*arr[n-pent1];
            }

            if (n - pent2 >= 0){
                arr[n] += coeff*arr[n-pent2];
            }
            arr[n] %= 1000000;
        }
    }
    return arr;
}

int main(int argc, char* argv[]){
    long N = strtol(argv[1], NULL, 10);
    long arr[N] = {0};
    long* partitions = computePartitions(arr, N);
    for(int i = 0; i < N; i++)
        cout << partitions[i] << endl;
    return 0;
}