#include <iostream>

int main() {
    int target = 0;
    std::cout << "Enter target for finding summations: ";
    std::cin >> target;

    int ways[target + 1] = {};
    ways[0] = 1;

    for(int i = 1; i <= target- 1; i++){
        for(int j = i; j <= target; j++){
            ways[j] += ways[j-i];
        }
    }

    std::cout << ways[target] << std::endl;

    return 0;
}
