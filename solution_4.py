f = open('input.txt', 'r')

for i in f.readlines():
    if len(i) >= 20:
        print(i)
f.close()