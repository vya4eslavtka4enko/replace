# PL = '{name}'
#
# with open('name.txt') as names_file:
#     names = names_file.readlines()
#     print(names)
#
# with open('letter.txt') as letter_text:
#     letter = letter_text.read()
#     for name in names:
#         print(name)
#         new_letter = letter.replace(PL, name)
#         print(new_letter)
import csv

# with open('Data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

with open('Data.csv') as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        print(row[1])
        temperature.append(row[1])
    print(temperature)
    for i in temperature:
        if i == "Temp":
            temperature.remove(i)
        else:
            pass
    print(temperature)
