#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
  char s[] = "A:4@r\%uL4Ff0f9b03=_cf0cc7fc2e_N";
  size_t length;
  int i;
  char tmp;
  
  length = strlen(s);
  for (i = 0; i < length; i = i + 1) {
    if ((' ' < s[i]) && (s[i] != '\x7f')) {
      tmp = (char)(s[i] + 0x2f);
      if (s[i] + 0x2f < 0x7f) {
        s[i] = tmp;
      }
      else {
        s[i] = tmp + -0x5e;
      }
    }
  }

  puts(s);
  return 0;
}
