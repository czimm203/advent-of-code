#include <cstdio>
#include <ios>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Range {
    int start, end;
};

class Line {
    public:
    Range left, right;

    Line(int x1, int y1, int x2, int y2) {
        this->left = Range{x1,y1};
        this->right = Range{x2,y2};
    }

    bool contains() {
        if(this->left.start <= this->right.start && this->left.end >= this->right.end) {
            return true;
        } else if(this->right.start <= this->left.start && this->right.end >= this->left.end) {
            return true;
        }
        return false;
    }
    bool overlaps() {
        if(this->left.start <= this->right.end && this->left.end >= this->right.start) {
            return true;
        }
        /* } else if(this->right.start <= this->left.start && this->right.end >= this->left.end) { */
        /*     return true; */
        /* } */
        return false;
    }
};

Line parseLine(string line) {
    string s,x;
    vector<int> tokens;
    stringstream ss(line);

    while(getline(ss, s, ',')) {
        stringstream second(s);
        while(getline(second, x, '-')) {
            tokens.push_back(stoi(x));
        }
    }
    
    return Line(tokens[0], tokens[1], tokens[2], tokens[3]);
}   

int main() {
    fstream file("input.txt");
    vector<string> lines;
    string line;
    
    if(file.is_open()) {
        while(file) {
            getline(file, line);
            lines.push_back(line);
        }
    }
    file.close();

    int count = 0;

    for (int i = 0; i < lines.size()-1; i++) {
        Line l = parseLine(lines[i]);
        bool contained = l.overlaps();
        cout << l.left.start << " " << l.left.end  << " " << l.right.start << " " << l.right.end <<  " " << contained << endl;
        if(contained) {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
