#include <cstddef>
#include <iostream>
#include <set>
#include <fstream>
#include <memory>
#include <stdexcept>
#include <string>

class Node {
    public:
    char value;
    std::shared_ptr<Node> next;

    Node(char v) {
        this->value = v;
        this->next = std::nullptr_t();
    }
};

class Queue {
    private:
        std::size_t capacity;
        std::shared_ptr<Node> head;
        std::shared_ptr<Node> tail;

    public:
        std::size_t size;
        Queue(int capacity) {
            this->head = std::shared_ptr<Node>(new Node('\0'));
            this->tail = this->head;
            this->capacity = capacity;
            this->size = 0;
        };

        char pop() {
            if(this->size <= 0) {
                throw std::runtime_error("Pop off empty queue\n");
            }
            auto n = this->head;
            char value = n->value;
            this->head = this->head->next;
            this->size--;
            std::cout << n.use_count() << std::endl;
            return n->value;
        };

        void push(char ch) {
            this->size++;
            if(this->size >= this->capacity) {
                this->pop();
            }
            std::shared_ptr<Node>n(new Node(ch));
            this->tail->next = n;
            this->tail = n;
        };

        bool all_unique() {
            std::string c = "";
            auto cur = this->head;
            while(cur != std::nullptr_t()) {
                if(c.find(cur->value) == std::string::npos) {
                    c+=cur->value;
                }
                cur = cur->next;
            }
            return c.size() == this->capacity && c[0] != '\0';
        };

        void print() {
            auto cur = this->head;
            while(cur != std::nullptr_t()) {
                std::cout << cur->value << "->";
                cur = cur->next;
            }
            std::cout << this->size << std::endl;
        };

};

int main(int argc, char* argv[]) {
    if(argc < 2) {
        std::cout << "Not enough arguments" << std::endl;
        exit(1);
    }
    std::fstream file(argv[1]);
    std::string packet;
    if(file.is_open()) {
        std::getline(file, packet);
    }

    auto q = Queue(14);
    int i = 0;
    for(auto c: packet) {
        i++;
        q.push(c);
        q.print();
        if(q.all_unique()) {
            std::cout << c << ": " << i << std::endl;
            break;
        }
    }
    return 0;
}
