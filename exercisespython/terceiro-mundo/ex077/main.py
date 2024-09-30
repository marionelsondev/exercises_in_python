palavras = ("aprender", "programar", "linguagem", "basquete", "estudar", "disciplina", "foco", "praticar", "programador", "futuro", "trabalhar", "tigre")

for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos ", end="")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
