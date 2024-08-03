phrase = str(input("Enter any phrase: ")).strip().upper()
joined_phrase = ''.join(phrase.split())
reversed_phrase = ''

for letter in range(len(joined_phrase) -1, -1, -1):
    reversed_phrase += joined_phrase[letter]
print(f"The reverse of {joined_phrase} is {reversed_phrase}")
if reversed_phrase == joined_phrase:
    print("The entered phrase is a palindrome.")
else:
    print("The entered phrase is not a palindrome.")
