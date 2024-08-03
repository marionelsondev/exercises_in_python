from datetime import date

list_people = []

for people in range(1, 8):
    birth_year = int(input(f"Enter the birth year of the {people}st person: "))
    list_people.append(date.today().year - birth_year)
print(f"{"-"*54}\nLIST OF PEOPLE WHO ARE ADULTS AND WHO ARE STILL MINORS\n{"-"*54}")
for age in range(0, 7):
    if list_people[age] < 21:
        print(f"The {age+1}st person is {list_people[age]} years old and is still a minor.")
    else:
        print(f"The {age+1}st person is {list_people[age]} years old and is already an adult.")
