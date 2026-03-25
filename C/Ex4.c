#include <stdio.h>
#include <locale.h>

int verificar(int num) {
    if (num % 2 == 0)
        return 1;
    
    else
        return 0;
    
}

int main() {
    int n;

    printf("Digite um número: ");
    scanf("%d", &n);

    if (verificar(n))
        printf("Par\n");

    else
        printf("Ímpar\n");

    return 0;

}