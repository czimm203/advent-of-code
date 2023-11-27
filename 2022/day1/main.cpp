#include <__functional/ranges_operations.h>
#include <_types/_uint64_t.h>
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string.h>
#include <vector>

std::vector<std::uint64_t> getMax(std::vector<std::string> lines) {
    uint64_t count = 0;
    std::vector<uint64_t> max;
    for( int i = 0; i < lines.size(); i++) {
        if( lines[i] != "" ) {
            count += std::stoi(lines[i]);
        } else {
            max.push_back(count);
            count = 0;
        }
    }
    std::sort(max.begin(), max.end(), std::ranges::greater());
    return max;
}

int main() {
    std::vector<std::string> data;
    std::string line;
    std::fstream file ("./input.txt");
    if(file.is_open()) {
        while(file) {
            std::getline(file, line);
            data.push_back(line);
        }
    }
    file.close();

    auto max = getMax(data);
    uint64_t top3 = max[0] + max[1] + max[2];
    std::cout << max[0] << "\n";
    std::cout << top3 << "\n";

    return 0;
}
