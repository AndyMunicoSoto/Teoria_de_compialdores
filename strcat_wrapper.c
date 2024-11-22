#include <string.h>
#include <stdlib.h>

char* strcat_wrapper(char* dest, const char* src) {
    return strcat(dest, src);
}
