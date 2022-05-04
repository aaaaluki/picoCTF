#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("[ERROR]: Enter a string to decode\n");
        return 1;
    }

    char* s;
    size_t length;
    int i;
    char tmp;

    s = strdup(argv[1]);
    length = strlen(s);
    for (i = 0; i < length; i = i + 1) {
        if ((' ' < s[i]) && (s[i] != '\x7f')) {
            tmp = (char)(s[i] + 0x2f);
            if (s[i] + 0x2f < 0x7f) {
                s[i] = tmp;
            } else {
                s[i] = tmp - 0x5e;
            }
        }
    }

  puts(s);
  return 0;
}
