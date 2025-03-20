text1 = 'результат операции: 42'
text2 = 'результат операции: 54'
text3 = 'результат работы программы: 209'
text4 = 'результат работы программы: 2'


def calc(textnumber):
    a = textnumber[textnumber.index(':'):]
    a1 = a[a.index(' '):]
    b = int(a1)
    print(b + 10)


calc(text1)
calc(text2)
calc(text3)
calc(text4)
