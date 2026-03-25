int a, *p, c;

/*a recebe o valor de 5*/

a = 5;

/* p recebe o endereço de a (p aponta para a)*/

p = &a;

/* posição de memória apontada por p recebe 6 */

*p = 6;

/* c recebe o valor armazenado na posição de memória apontada por p */

c = *p;
