produtos = ("Bola de basquete", 79.90, 
            "Tênis", 899, 
            "Notebook Legion slim 5i", 6063.99, 
            "Moletom GAP", 307, "Lanterna", 20, 
            "Monitor 27'", 779, 
            "Honda Civic SI 2007", 79000, 
            "Yamaha mt-07", 45599)
print(41*"-")
print(f"{10*' '}LISTAGEM DE PREÇOS{10*' '}")
print(41*"-")
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}", end="")
    else:
        print(f"R$ {produtos[pos]:>8.2f}")
print(41*"-")
