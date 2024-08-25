print(f"{30*'-'}\n{6*' '}Sequência de Fibonacci{6*' '}\n{30*'-'}")
n = int(input("Quantos elementos deseja visualizar? "))
t1 = 0
t2 = 1
cont = 3
print(f"{t1} ⭢ {t2}", end="")
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f" ⭢ {t3}", end="")
    cont += 1
print(" ⭢ FIM\n", end="")
