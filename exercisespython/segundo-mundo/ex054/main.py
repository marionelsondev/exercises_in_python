from datetime import date

current_year = date.today().year
totsmaller = 0
totbigger = 0
list_people = []

for people in range(1, 8):
    birth_year = int(input(f"Enter the birth year of the {people}st person: "))
    age = current_year - birth_year
    if age < 21:
        totsmaller += 1
    else:
        totbigger += 1
print(f"In total, we had {totsmaller} minors.")
print(f"And we also had {totbigger} adults.")
