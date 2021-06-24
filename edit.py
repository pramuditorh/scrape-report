with open('rule.txt') as f:
    id = ''
    lines = f.readlines()
    for line in lines:
        id = line.split(' ')[0]
        print(id)