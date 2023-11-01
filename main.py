PL = '{name}'

with open('name.txt') as names_file:
    names = names_file.readlines()
    print(names)

with open('letter.txt') as letter_text:
    letter = letter_text.read()
    for name in names:
        print(name)
        new_letter = letter.replace(PL, name)
        print(new_letter)