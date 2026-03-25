#include <stdio.h>

/* Variavel simples */
int a;

/* Variavel ponteiro */
int *p;

/* Variavel simples */
int b;

int main(void) {
    a = 10;
    p = &a; // p aponta para o endereço de a que e importante analisar
    b = *p + 5;
    printf("a: %d\n", a);
    printf("a: %p\n", p);
    printf("a: %d\n", b);

}