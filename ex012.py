from math import sqrt
cat1 = float(input('Digite um cateto: '))
cat2 = float(input('Digite outro cateto:'))
hip = cat1**2 + cat2**2
hip2 = sqrt(hip)

print('A hipotenusa é {:.2f}'.format(hip2))
