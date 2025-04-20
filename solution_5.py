f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')

for i in range(len(f)):
    if '\n' in f[i]:
       f[i] = f[i][0:-1]
print(f)


try:
    answer = float(f[0])/float(f[1])+float(f[2])
    fn.write(str(answer))
except ValueError:
    fn.write('data error')
except ZeroDivisionError:
    fn.write('division by 0')