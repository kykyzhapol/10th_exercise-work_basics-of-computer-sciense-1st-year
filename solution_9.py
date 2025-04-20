import os

f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')

for i in range(len(f)):
    if i%2 == 1:
        fn.write(f[i])

os.makedirs('simple', exist_ok = True)
fn.close()
os.replace("output.txt", "simple/output.txt")