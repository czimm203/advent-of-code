#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <string.h>


char outcome [3] = {'X', 'Y', 'Z'};

class Game {
    public:
        std::vector<std::string> rounds;
        uint64_t score;
        Game(std::vector<std::string> rounds) {
            this->rounds = rounds;
            this->score = 0;
        };

        void evaluatePVP() {
            for(int i = 0; i < this->rounds.size()-1; i++) {
                char playerMove = this->rounds[i][2];
                for(int i = 0; i < 3; i++) {
                    if(playerMove == outcome[i]) {
                        this->score += i + 1;
                    }
                }
                if(playerMove == 'X'){
                    if(this->rounds[i][0] == 'A') {
                        this->score += 3;
                    } else if(this->rounds[i][0] == 'C') {
                        this->score += 6;
                    }
                }
                else if(playerMove == 'Y'){
                    if(this->rounds[i][0] == 'B') {
                        this->score += 3;
                    } else if(this->rounds[i][0] == 'A') {
                        this->score += 6;
                    }
                }
                else if(playerMove == 'Z'){
                    if(this->rounds[i][0] == 'C') {
                        this->score += 3;
                    } else if(this->rounds[i][0] == 'B') {
                        this->score += 6;
                    }
                }
            } 
        }

        void evaluateFixed() {
            for(int i = 0; i < this->rounds.size()-1; i++) {
                char outcome = this->rounds[i][2];
                if(outcome == 'X'){
                    if(this->rounds[i][0] == 'A') {
                        this->score += 3;
                    } else if(this->rounds[i][0] == 'B') {
                        this->score += 1;
                    } else if(this->rounds[i][0] == 'C') {
                        this->score += 2;
                    }
                }
                else if(outcome == 'Y'){
                    if(this->rounds[i][0] == 'A') {
                        this->score += 4;
                    } else if(this->rounds[i][0] == 'B') {
                        this->score += 5;
                    } else if(this->rounds[i][0] == 'C') {
                        this->score += 6;
                    }
                }
                else if(outcome == 'Z'){
                    if(this->rounds[i][0] == 'A') {
                        this->score += 8;
                    } else if(this->rounds[i][0] == 'B') {
                        this->score += 9;
                    }else if(this->rounds[i][0] == 'C') {
                        this->score += 7;
                    }
                }
            } 
        }
};


int main() {
    std::fstream file("./input.txt");
    std::string line;
    std::vector<std::string> lines;
    if(file.is_open()) {
        while(file) {
            std::getline(file, line);
            lines.push_back(line);
        }
    }       

    Game g(lines);
    g.evaluateFixed();

    std::cout << g.score << "\n";
    return 0;
}
