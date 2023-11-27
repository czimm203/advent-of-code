#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>

using namespace std;

char getPrio(string l) {
    int half = l.size()/2;
    string p1 = l.substr(0, half);
    string p2 = l.substr(half, l.size());

    set<char> chars1;
    set<char> chars2;

    for(int i = 0; i < half; i++) {
        chars1.insert(p1[i]);
        chars2.insert(p2[i]);
    }
    for(auto ch1 = chars1.begin(); ch1 != chars1.end(); ch1++) {
        if(chars2.count(*ch1) == 1) {
            return *ch1;
        }
    }
    return ' ';
}

int decodePrio(char c) {
    int v = int(c);
    if(v >=97 && v <= 122) {
        return v - 96;
    } else if(v >= 65 && v <= 132) {
        return v - 38;
    } 
    return -1;
}

int part1(vector<string> lines) {
    int score = 0;
    for(auto l: lines) {
        char p = getPrio(l);
        int s = decodePrio(p);
        if(s == -1) {
            exit(1);
        }
        score += s;
    }
    return score;
}

void part2(vector<string> lines) {
    int numGroups = lines.size()/3;
    int score = 0;
    set<char> s1;
    set<char> s2;
    set<char> s3;

    
    for(int i = 0; i < numGroups; i++) {
        for(int j = 0; j < lines[i*3].length(); j++){
            s1.insert(lines[i*3][j]);
        }
        for(int j = 0; j < lines[i*3+1].length(); j++){
            s2.insert(lines[i*3+1][j]);
        }
        for(int j = 0; j < lines[i*3+2].length(); j++){
            s3.insert(lines[i*3+2][j]);
        }

        for(auto ch = s1.begin(); ch != s1.end(); ch++) {
            if( s2.count(*ch) == 1 && s3.count(*ch) == 1 ) {
                cout << *ch << endl;
                score += decodePrio(*ch);
            }
        }
        s1 = set<char>();
        s2 = set<char>();
        s3 = set<char>();
    }
    cout << score << "\n";

}

int main() {
    fstream file("./input.txt");
    string line;
    vector<string> lines;
    if(file.is_open()) {
        while(file) {
            getline(file, line);
            if(line != "") {
                lines.push_back(line);
            }
        }
    }
    file.close();

    part2(lines);

    return 0;
}

