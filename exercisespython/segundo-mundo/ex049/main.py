num_tab = int(input("Digite o número que deseja tabular: "))
print(f"{" "*2}TABUADA DO {num_tab}\n{"-"*16}")

for multiplicador in range(1, 11):
    print(f"{num_tab} X {multiplicador} = {num_tab*multiplicador}")
print(f"{"-"*16}")
