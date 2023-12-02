#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int BUF_SIZE = 64;
int char2int(char c) {
    int n = (int)c - 48;
    if(n < 0 || n > 9) {
        return -1;
    }
    return n;
}

int calc_value(char *buf) {
    int len = strlen(buf);
    int start = -1, end = -1;
    for(int i = 0; i < len-1; i++) {
        int n = char2int(buf[i]);
        if(n != -1) {
            end = n;
            if(start == -1) {
                start = n;
            }
        }
    }
    return start*10 + end;
}

int find_str(char *haystack, char* needle) {
    char *found = strstr(haystack,needle);
    if(found == NULL) {
        return -1;
    }
    return found - haystack;
}

void part1(char *path) {
    FILE *f = fopen(path, "r");
    if(f == NULL) {
        printf("failed to open file\n");
        exit(1);
    }
    char buf[BUF_SIZE];
    int total = 0;
    while(fgets(buf, BUF_SIZE, f) != NULL) {
        int n = calc_value(buf);
        total += n;
    }
    printf("Part 1: %d\n", total);
}

struct Marker {
    int place;
    int token_index;
};

void part2(char *path) {
    FILE *f = fopen(path, "r");
    if(f == NULL) {
        printf("failed to open file\n");
        exit(1);
    }
    char *buf = malloc(sizeof(char)*BUF_SIZE);
    char *buf2 = malloc(sizeof(char)*BUF_SIZE);
    int total = 0;
    char* tokens[] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    while(fgets(buf, BUF_SIZE, f) != NULL) {
        struct Marker first =  {-1,-1};
        struct Marker last =  {-1,-1};
        for(int i=0; i < 20; i++) {
            strcpy(buf2, buf);
            int idx = find_str(buf2, tokens[i]);
            int offset = 0;
            while(idx != -1) {
                if(idx + offset > last.place) {
                    last.place = idx + offset;
                    last.token_index = i;
                }
                if(idx + offset < first.place || first.place == -1) {
                    first.place = idx + offset;
                    first.token_index = i;
                }
                buf2 += idx+strlen(tokens[i]);
                offset += idx+strlen(tokens[i]);
                idx = find_str(buf2, tokens[i]);
            }
        }
        printf("%s {first: %d, last: %d}\n", buf, first.token_index, last.token_index);
        total += (first.token_index%10) * 10 + (last.token_index%10);
    }
    printf("Part 2: %d\n", total);
}

int main(int argc, char *argv[]) {
    if(argc <= 1) {
        printf("please provide file path");
        return 1;
    }
    part1(argv[1]);
    part2(argv[1]);
    return 0;
}
