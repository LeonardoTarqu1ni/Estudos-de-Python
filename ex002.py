n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
s = n1+n2
#print('A soma vale entre', n1, 'e', n2, 'é', s) substituido pelo .format
print('A soma entre {} e {} vale {}'.format(n1, n2, s))