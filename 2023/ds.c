#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

const size_t INITIAL_DARRAY_SIZE = 32;

typedef struct {
    size_t len;
    size_t capacity;
    char values[INITIAL_DARRAY_SIZE][255];
}DynamicArray;

DynamicArray make_dynamic_array() {
    char buf[INITIAL_DARRAY_SIZE][255] = {0};
    DynamicArray da = {
        0,
        INITIAL_DARRAY_SIZE,
        
    };
    return da;
}

void da_append(DynamicArray *da, char value[255]) {
    assert(da != NULL);
    if(da->len >= da->capacity) {
        
    }
    da->values[da->len+1] = value;
    da->len += 1;
}
