f = open('input.txt', 'r')
fn = open('output.txt', 'w')

for i in f:
    if '100' == i:
        pass
    else:
        fn.write(f'{i}')