while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    print("-"*30)
    if num < 0:
        break
    for multiplicador in range(1, 11):
        print(f"{num} X {multiplicador} = {num*multiplicador}")
    print("-"*30)
print("PROGRAMA TABUADA ENCERRADO.")
