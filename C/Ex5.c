#include <stdio.h>

int main() {
    float notas[4];
    float soma = 0;
    float maior, menor;
    int i;

    for (i = 0; i < 4; i++) {
        printf("Digite a nota %d: ", i + 1);
        scanf("%f", &notas[i]);
        soma += notas[i];
    }

    maior = menor = notas[0];

    for (i = 1; i < 4; i++) {
        if (notas[i] > maior)
            maior = notas[i];

        if (notas[i] < menor)
            menor = notas[i];
    }

    printf("Média: %.2f\n", soma / 4);
    printf("Maior: %.2f\n", maior);
    printf("Menor: %.2f\n", menor);

    return 0;
}