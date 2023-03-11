x  = 0
y = 0
pal = 0
while x <= 100:
    y = x
    while y <= 100:
        temp = str(x * y)
        tempInverso = temp[::-1]
        if temp == tempInverso:
            palTemp = int(temp)
            if palTemp > pal:
                pal = palTemp
        y += 1
    x += 1
print('O maior palíndromo encontrado foi', pal)
