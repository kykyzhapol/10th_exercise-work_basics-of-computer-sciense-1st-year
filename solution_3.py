f = open('input.txt', 'r')

for i in f.readlines():
    print(i[0], end='')
f.close()