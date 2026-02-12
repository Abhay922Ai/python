import itertools

name = input("Enter name: ")
year = input("Enter year: ")
college = input("Enter college short name: ")
roll = input("Enter last 4 digits of roll: ")

symbols = ["@", "#", "$", "_", "123"]

base_words = [
    name.lower(),
    name.capitalize(),
    college.lower(),
    college.capitalize(),
]

numbers = [year, roll]

combinations = []

for word in base_words:
    for num in numbers:
        for sym in symbols:
            combinations.append(word + num + sym)
            combinations.append(sym + word + num)

print("\nGenerated Passwords:\n")

for i, pwd in enumerate(combinations[:100], 1):
    print(f"{i}. {pwd}")
