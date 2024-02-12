import csv
with open('wares.csv', 'r', encoding='utf=8') as file:
    reader = csv.DictReader(file, delimiter=";")
    data = list(reader)
    for line_dict in data:
        old = int(line_dict['Old price'])
        new = int(line_dict['New price'])
        if old > new:
            print(f'{line_dict["Name"]}, old price = {old}, new price {new}')
