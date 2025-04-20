f = open('input.txt', 'r')

for i in f.readlines():
    if i[0].lower() == 'a':
        print(i)
f.close()