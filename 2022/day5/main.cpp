#include <_types/_uint64_t.h>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <sstream>
#include <memory>
#include <string>
#include <vector>

template<typename T>
struct Node {
    T value;
    std::unique_ptr<Node<T>> prev;
};

template<typename T>
class Stack {
    public:
        Stack() {
            this->size = 0;
            this->last = std::nullptr_t();
        };
        ~Stack() {
            while(!this->is_empty()) {
                this->pop();
            }
        };
        T pop() {
            if(this->size != 0) {
                auto n = std::move(this->last);
                this->last = std::move(n->prev);
                T data = n->value;
                this->size--;
                return data;
            } else {
                throw std::runtime_error("Trying to pop off empty stack");
            }
        };      
        void push(T value) {
            this->last = std::unique_ptr<Node<T>>(new Node<T>{value, std::move(this->last)});
            this->size++;
        };

        bool is_empty() {
            return this->size == 0 ? true : false;
        };
    
    private:
        uint64_t size;
        std::unique_ptr<Node<T>> last;
};

struct InstructionSet {
    int count;
    int loc;
    int dest;
};

int main(int argc, char* argv[]) {
    if(argc < 2) {
        std::cout << "Not Enough arguments" << std::endl;
        return 1;
    }
    
    std::fstream file(argv[1]);
    std::vector<std::string> data;
    std::vector<std::string> instructions;
    std::string line;
    bool parsedData = false;

    if(file.is_open()) {
        while(file) {
            getline(file, line);
            if(line.size() == 0) {
                parsedData = true;
                continue;
            };
            if(!parsedData) {
                data.push_back(line);
            } else {
                instructions.push_back(line);
            }
        }
    }

    int len = (data[0].size()+1)/4;
    Stack<char> stacks[len];

    for(int i = data.size() - 2; i >= 0; i--) {
        std::string line = data[i];
        if(line.length() != 0) {
            for(int j = 0; j < len; j++) {
                char letter = line[j*4+1];
                if(letter != ' ') {
                    stacks[j].push(letter);
                }
            }
        }
    }

    std::vector<InstructionSet> instructionList;

    for(auto line: instructions) {
        std::stringstream ss(line);
        std::string str;
        int count;
        int original;
        int dest;
        int c = 0;

        while(std::getline(ss, str, ' ')) {
            if(c == 1) {
                count = std::stoi(str);
            } else if(c == 3) {
                original = std::stoi(str);
            } else if(c == 5) {
                dest = std::stoi(str);
                instructionList.push_back(InstructionSet{count, original, dest});
                std::cout << count << original << dest << "\n";
            }
            c++;
        }
    }
    
    Stack<char>(ph);
    for(auto instruction: instructionList) {
        for(int i = 0; i < instruction.count; i ++) {
            ph.push(stacks[instruction.loc-1].pop());
        }
        while(!ph.is_empty()) {
            stacks[instruction.dest-1].push(ph.pop());
        }
    }

    for(int i = 0; i < len; i++) {
        std::cout<<stacks[i].pop()<<"\n";
    }
    return 0;
}
