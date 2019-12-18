#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <cmath>
using namespace std;

int main() {
    ifstream infile;
    infile.open("p099_base_exp.txt");

    if(!infile){
        cout << "Cannot open input file" << endl;
        return 1;
    }

    map<long, int> base_pairs;

    string row;
    int i = 1;
    vector<long> terms;
    while(infile.good()){
        getline(infile, row);
        stringstream ss(row);
        for(int j; ss >> j;){
            terms.push_back(j);
            if (ss.peek() == ',') {
                ss.ignore();
            }
        }
        base_pairs[terms[1]*log(terms[0])] = i;
        terms.clear();
        i++;
    }

    cout << (--base_pairs.end())->first << endl;
    cout << (--base_pairs.end())->second << endl;



    return 0;
}
