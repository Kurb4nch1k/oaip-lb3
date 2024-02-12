n = int(input())
with open('vps.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    data = list(reader)[1:]
    print('\n'.join(map(lambda x: x[0], [i for i in data if int(i[-2]) >= n])))

