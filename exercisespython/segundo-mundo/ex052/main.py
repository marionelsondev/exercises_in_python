num = int(input("Enter an integer: "))
tot = 0

for c in range(1, num+1):
    if num % c == 0:
        print(f"\033[0;33m{c}\033[m ", end="")
        tot += 1
    else:
        print(f"\033[0;31m{c}\033[m ", end="")
print(f"\nThe number {num} was divisible {tot} times.")
if num % 1 == 0 and num % num == 0 and tot == 2:
    print("That's why it's PRIME!")
else:
    print("And that's why it's not PRIME!")
