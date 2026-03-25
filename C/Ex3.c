#include <stdio.h>
#include <string.h>

struct Interno {
    char m2[20];
};

struct Externo {
    struct Interno m1;
};

int main() {
    struct Externo obj;

    strcpy(obj.m1.m2, "Olá Mundo");

    printf("%s\n", obj.m1.m2);

    return 0;
}
