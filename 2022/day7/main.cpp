#include <_types/_uint32_t.h>
#include <_types/_uint64_t.h>
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

template<typename T>
class List {
    public:
        T values[50];
        uint64_t size;

        void append(T val) {
            values[size] = val;
            size++;
        }
};

struct File {
    std::string name;
    uint32_t size;
};

struct Directory {
    std::string name;
    Directory *parent;
    List<Directory*>* child_dirs;
    List<File*>* files;
};

class FileTree {
    public:
    Directory root;
    Directory *cwd;

    void parse_instruction(std::string instruction) {
        std::stringstream ss(instruction);
        std::vector<std::string> tokens;
        std::string token;
        while(std::getline(ss, token, ' ')) {
            tokens.push_back(token);
        }
        if(tokens[0] == "$") {
            if(tokens[1] == "cd" && tokens[2] == "..") {
                std::cout << "cd .." << "\n";
                cwd = cwd->parent;
            } else if(tokens[1] == "ls") {
                std::cout << "ls" << "\n";
                return;
            } else {
                std::cout << "seaching for " << tokens[2] << "\n";
                for(int i = 0; i< cwd->child_dirs->size; ++i) {
                    std::cout << i << "\n";
                    auto child = cwd->child_dirs->values[i];
                    std::cout << tokens[2] << cwd->child_dirs->values[i]->name << "\n";
                    if(child->name == tokens[2]) {
                        std::cout << "found " << cwd->child_dirs->values[i]->name<< "\n";
                        cwd = child;
                        std::cout << this->cwd << " " << child << "\n";
                    }
                }
            }
        } else if(tokens[0] == "dir") {
            auto dirs = new List<Directory*>();
            auto files = new List<File*>();
            auto d = new Directory{tokens[1], cwd, dirs, files};
            std::cout << "adding " << d->name << " to " << cwd->name << " " <<cwd->child_dirs->size <<"\n";
            cwd->child_dirs->append(d);
        } else {
            auto f = new File{tokens[1], (uint32_t)std::stoi(tokens[0])};
            std::cout << "adding " << f->name << " to " << cwd->name<< " " << cwd->files->size<<"\n";
            cwd->files->append(f);
        }
    }
};

int main(int argc, char* argv[]) {
    if(argc != 2) {
        exit(1);
    }

    std::string line;
    std::vector<std::string> lines;
    std::fstream FILE(argv[1]);
    if(FILE.is_open()) {
        while(std::getline(FILE, line)) {
            lines.push_back(line);
        }
    }

    std::cout<< "ha\n";
    auto dirs = new List<Directory*>();
    auto files = new List<File*>();
    Directory *root = new Directory{"/", std::nullptr_t(), dirs, files};
    FileTree ft = FileTree{*root, root};
    
    for(int i = 0; i < lines.size(); i++) {
        ft.parse_instruction(lines[i]);
    }

    std::cout << ft.root.child_dirs->size << "\n";
    for(int i = 0 ; i < ft.root.child_dirs->size; i++) {
        std::cout << i <<ft.root.child_dirs->values[i]->name << "\n";
    }
}   
