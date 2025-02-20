text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'
a = text1[text1.index(':'):]
a1 = a[a.index(' '):]
b = int(a1)
print(b + 10)

c = text2[text2.index(':'):]
c1 = c[c.index(' '):]
d = int(c1)
print(d + 10)

e = text3[text3.index(':'):]
e1 = e[e.index(' '):]
f = int(e1)
print(f + 10)
