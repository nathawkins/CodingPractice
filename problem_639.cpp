#include <iostream>
using std::cout; using std::endl;
#include <vector>
using std::vector;
#include <cmath>
using std::sqrt; using std::pow;
#include <set>
using std::set;
#include <ctime>
using std::clock;

vector<long> primeFactorization(long N){
    vector<long> factorization;

    while(N%2 == 0){
        factorization.push_back(2);
        N /= 2;
    }


    for(long i = 3; i <= sqrt(N); i +=2){
        while(N % i == 0){
            factorization.push_back(i);
            N /= i;
        }
    }

    if(N > 2){
        factorization.push_back(N);
    }

    set<long> s(factorization.begin(), factorization.end());
    vector<long>().swap(factorization);
    vector<long> to_return(s.begin(), s.end());
    set<long>().swap(s);
    return to_return;
}


long fk(long i, int k){
    if(i == 1){
        return 1;
    }
    else{
        vector<long> factors = primeFactorization(i);
        long prod = 1;
        for(auto val: factors){
            prod *= pow(val, k);
        }
        vector<long>().swap(factors);
        return prod;
    }
}

unsigned long long Sk(unsigned long long A, int k){
    unsigned long long total = 0;

    for(unsigned long long i = 1; i <= A; i++){
        total += fk(i, k); 
    }
    return total;

}

unsigned long long Gk(unsigned long long A, int N){
    unsigned long long total = 0;

    for(int k = 1; k <= N; k++){
        cout << k << endl;
        total += Sk(A, k);
    }
    return total;
}

int main(){
    //Test Cases
    cout << std::boolalpha;
    cout << (fk(2, 1) == 2) << endl;
    cout << (fk(4,1) == 2) << endl;
    cout << (fk(18,1) == 6) << endl;
    cout << (fk(18,2) == 36) << endl;

    cout << (Sk(10, 1) == 41) << endl;
    cout << (Sk(100, 1) == 3512) << endl;
    cout << (Sk(100, 2) == 208090) << endl;
    cout << (Sk(10000, 1) == 35252550) << endl;


    cout << (Gk(3,3) == 56) << endl;

    clock_t start = clock();

    cout << (Gk(1E8, 3) % 1000000007 == 338787512) << endl;

    clock_t end = clock();
    cout << double(end - start) / CLOCKS_PER_SEC << endl;
}