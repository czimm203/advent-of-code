#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const size_t BUF_SIZE = 256;

int find_str(char* haystack, char* needle) {
    char *find = strstr(haystack, needle);
    if(find == NULL) {
        return -1;
    }
    return find - haystack;
}

int valid_game(char *game_str) {
    int offset = find_str(game_str, ":") + 2;
    game_str += offset;
    char *round_str = strtok(game_str, " ");
    int max_red = 12, max_green =13 , max_blue = 14;
    int i = 0;
    int n = 0;
    while(round_str != NULL) {
        if(i % 2 == 0) {
            n = atoi(round_str);    
        } else {
            char c = round_str[0];
            if(c == 'r' && n > max_red) {
                return 0;
            } else if(c == 'g' && n > max_green) {
                return 0;
            } else if(c == 'b' && n > max_blue) {
                return 0;
            }
        }
        i++;
        round_str = strtok(NULL, " "); 
    }
    return 1;
}

int power(char *game_str) {
    int offset = find_str(game_str, ":") + 2;
    game_str += offset;
    char *round_str = strtok(game_str, " ");
    int max_red = 0, max_green = 0 , max_blue = 0;
    int i = 0;
    int n = 0;
    while(round_str != NULL) {
        if(i % 2 == 0) {
            n = atoi(round_str);    
        } else {
            char c = round_str[0];
            if(c == 'r' && n > max_red) {
                max_red = n;
            } else if(c == 'g' && n > max_green) {
                max_green = n;
            } else if(c == 'b' && n > max_blue) {
                max_blue = n;
            }
        }
        i++;
        round_str = strtok(NULL, " "); 
    }
    return max_red*max_blue*max_green;
}

void part1(char *path) {
    FILE *f = fopen(path,"r");
    char *buf = malloc(sizeof(char)*BUF_SIZE);
    int total = 0;
    int i = 1;
    while(fgets(buf, BUF_SIZE, f) != NULL) {
        int valid = valid_game(buf);
        if(valid == 1) {
            total += i;
        }
        i++;
    }
    fclose(f);
    printf("part1: %d\n", total);
}

void part2(char *path) {
    FILE *f = fopen(path,"r");
    char *buf = malloc(sizeof(char)*BUF_SIZE);
    int total = 0;
    int i = 1;
    while(fgets(buf, BUF_SIZE, f) != NULL) {
        int p = power(buf);
        total += p;
        i++;
    }
    fclose(f);
    printf("part2: %d\n", total);
}

int main(int argc, char *argv[]) {
    if(argc <= 1) {
        printf("Please provide path");
        return 1;
    }
    part1(argv[1]);
    part2(argv[1]);
    return 0;
}
