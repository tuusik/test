def F(x):
    return str(x)[0] == str(x)[-1]
def M(x):
    return len(str(x)) == 5 and str(x)[1] == "7"

f = open("17.txt")
a = [int(x) for x in f]
s = 0
cnt = 0
for i in range(len(a) - 2):
    first = a[i]
    second = a[i + 1]
    third = a[i + 2]
    if sum(F(x) for x in [first, second, third]) == 1:
        if sum(M(x) for x in [first, second, third]) == 2:
            cnt += 1
            s += max(first, second, third)

print(cnt, s)
