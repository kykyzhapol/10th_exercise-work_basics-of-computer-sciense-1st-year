import datetime

f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')

now = datetime.date(2025, int(list(f[0].split(sep='.'))[0]), int(list(f[0].split(sep='.'))[1]))

lagged = {}
for i in f[2:]:
    lagged[list(i.split())[0]] = datetime.date(2025, int(list(list(i.split())[1].split(sep='.'))[0]), int(list(list(i.split())[1].split(sep='.'))[1]))

for i in range(len(lagged)):
    if now - i > 3 and i.index() > 1000:
        fn.write(i)


print(lagged)
