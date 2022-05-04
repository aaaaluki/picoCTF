#include <openssl/md5.h>
#include <stdio.h>
#include <string.h>


int main(int argc, char** argv) {
    const char *sample_flag = "picoCTF{br1ng_y0ur_0wn_k3y_";
    size_t str_len;
    unsigned char hash[16];
    char hash_hex[32];
    char flag[40];
    MD5_CTX context;

    // Compute MD5 hash
    MD5_Init(&context);
    MD5_Update(&context, sample_flag, strlen(sample_flag));
    MD5_Final(hash, &context);

    // Get MD5 hash as hex representation
    int step = 0;
    int i;
    for (i = 0; i < 16; i = i + 1) {
        sprintf(hash_hex + step,"%02x",hash[i]);
        step = step + 2;
    }

    // Generate the flag
    int j;
    for (j = 0; j < 27; j++) {
        flag[j] = sample_flag[j];
    }
    flag[27] = hash_hex[18];
    flag[28] = hash_hex[26];
    flag[29] = hash_hex[25];
    flag[30] = hash_hex[0];
    flag[31] = hash_hex[26];
    flag[32] = hash_hex[18];
    flag[33] = hash_hex[12];
    flag[34] = hash_hex[26];
    flag[35] = '}';

    printf(flag);

    return 0;
}
