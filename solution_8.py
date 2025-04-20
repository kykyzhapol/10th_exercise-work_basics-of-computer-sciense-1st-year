f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')

for i in range(len(f)):
    if '\n' in f[i]:
       f[i] = f[i][0:-1]

fn.write(sum(int(f[0:31]))/31)
fn.write(sum(int(f[31:59]))/28)
fn.write(sum(int(f[59:90]))/31)
fn.write(sum(int(f[90:120]))/30)
fn.write(sum(int(f[120:151]))/31)
fn.write(sum(int(f[151:181]))/30)
fn.write(sum(int(f[181:212]))/31)
fn.write(sum(int(f[212:243]))/31)
fn.write(sum(int(f[243:273]))/30)
fn.write(sum(int(f[273:304]))/31)
fn.write(sum(int(f[304:334]))/30)
fn.write(sum(int(f[334:365]))/31)