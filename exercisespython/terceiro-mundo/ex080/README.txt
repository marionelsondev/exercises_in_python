Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

Raciocínio:

1. Utilize o loop for para ler 5 números inteiros -
2. Verificar se esse número vai ser adicionado no início, meio ou fim da lista -
    Início e fim:
        - Se for o primeiro número digitado ou o número digitado for maior que o último número da lista. Adicione o número no final.
    Meio:
        - Utilizar um loop while para percorrer a lista utilizando uma variavel auxiliar "posicao" com o valor de 0
        - Verificar se o valor digitado é menor ou igual ao valor que está na posição 0. Se for ele vai ser adicionado naquela posição. Caso contrário a variável "posicao" recebe +1 e é feito todo o processo novamente até o número ser inserido usando o insert.
3. Mostre a lista ordenada ao usuário -
