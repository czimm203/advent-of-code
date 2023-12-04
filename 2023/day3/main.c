#include <ctype.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const size_t MAX_BUF = 256;
struct contents {
    int num;
    char lines[256][256];
};

struct contents read_file(char* path) {
    struct contents contents = {0};
    FILE* f = fopen(path, "r");
    char* buf = malloc(sizeof(char)*MAX_BUF);
    while(fgets(buf, MAX_BUF, f)) {
        strncpy(contents.lines[contents.num], buf, MAX_BUF);
        contents.num++;
    }
    fclose(f);
    return contents;
}

bool is_part(char c) {
    return strchr("0123456789.\n\0", c) == NULL;
}

bool is_gear(char c) {
    return c == '*';
}

void part1(char* path) {
    struct contents c = read_file(path);
    char buf[16] = {0};
    int total = 0, n = 0;
    for(int j = 0; j < c.num; j++) {
        int left = -1, right = -1;
        for(int i = 0; i < strlen(c.lines[j]); i++) {
            char cur = c.lines[j][i];
            if(isdigit(cur)){
                if(left == -1) {
                    buf[0] = cur;
                    left = i;
                    right = i;
                    n++;
                } else {
                    buf[n] = cur;
                    right = i;
                    n++;
                }
            } else {
                if(right != -1) {
                    int min_x = left > 0 ? left-1 : 0;
                    int min_y = j > 0 ? j - 1 : 0;
                    int max_x = right < strlen(c.lines[j]) - 1 ? right + 1 : strlen(c.lines[j]) - 1;
                    int max_y = j < c.num ? j + 1 : c.num;
                    /* printf("%s x: %d, y: %d, X: %d, Y: %d\n", buf, min_x, min_y, max_x, max_y); */
                    int value = atoi(buf);
                    bool add_to_total = false;
                    for(int x = min_x; x <= max_x; x++) {
                        for(int y = min_y; y <= max_y; y++) {
                            if(is_part(c.lines[y][x])) {
                                add_to_total = true;
                            }
                        }
                    }
                    if(add_to_total) total += value;
                    left = -1;
                    right = -1;
                    n = 0;
                    for(int z = 0; z < 16; z++){ 
                        buf[z] = '\0';
                    }
                }
            }
        }
    }
    printf("Part 1: %d\n", total);
}

struct Num_range {
    int y;
    int x0;
    int x1;
    int value;
};

struct Ranges {
    int num;
    struct Num_range ranges[2048];
};

struct Gear {
    int x;
    int y;
};

struct Gears {
    int num;
    struct Gear gears[2048];
};

void part2(char* path) {
    struct contents c = read_file(path);
    struct Ranges ranges = {0};
    struct Gears gears = {0};
    char buf[16] = {0};
    int n = 0;
    unsigned long total = 0;
    for(int j = 0; j < c.num; j++) {
        int left = -1, right = -1;
        for(int i = 0; i < strlen(c.lines[j]); i++) {
            char cur = c.lines[j][i];
            if(isdigit(cur)){
                if(left == -1) {
                    buf[0] = cur;
                    left = i;
                    right = i;
                    n++;
                } else {
                    buf[n] = cur;
                    right = i;
                    n++;
                }
            } else {
                if(right != -1) {
                    int value = atoi(buf);
                    struct Num_range r = {j,left,right,value};
                    ranges.ranges[ranges.num] = r;
                    ranges.num++;
                    left = -1;
                    right = -1;
                    n = 0;
                    for(int z = 0; z < 16; z++){ 
                        buf[z] = '\0';
                    }
                }
                if(is_gear(cur)) {
                    struct Gear g = {i,j};
                    gears.gears[gears.num] = g;
                    gears.num++;
                }
            }
        }
    }
    /* for(int i = 0; i < ranges.num; i++) { */
    /*     struct Num_range r = ranges.ranges[i]; */
    /*     printf("{y: %d, x0: %d, x1: %d, value: %d}\n", r.y, r.x0, r.x1, r.value); */
    /* } */
    for(int i = 0; i<gears.num; i++){
        int ratio = 1;
        int num = 0;
        struct Gear g = gears.gears[i];
        /* printf("{y: %d, x: %d}\n", g.y, g.x); */
        for(int j = 0; j < ranges.num; ++j) {
            struct Num_range r = ranges.ranges[j];
            if(g.y <= r.y+1 && g.y >= r.y-1 && g.x >= r.x0-1 && g.x <= r.x1+1) {
                /* printf("ratio %d, value %d\n", ratio, r.value); */
                num++;
                ratio *= r.value;
            }
        }
        if(num == 2) {
            /* printf("{x: %d, y: %d}\n", g.x, g.y); */
            total += ratio;
        }
        ratio = 1;
        num = 0;
    }
    printf("Part 2: %lu\n", total);
}

int main(int argc, char* argv[]) {
    if(argc < 2) {
        printf("Enter path\n");
        return 1;
    }
    part1(argv[1]);
    part2(argv[1]);
    return 0;
}
