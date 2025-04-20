f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')
print(len(f), f[0][0:-1])
try:
    if len(f)-1 == int(f[0][0:-1]):
        fn.write('YES')
    else:
        fn.write('NO')
except:
    fn.write('ERROR')
fn.close()