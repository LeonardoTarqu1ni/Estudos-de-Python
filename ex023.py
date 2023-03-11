nome = str(input('Ola, qual seu nome?'))
salario = float(input(f'{nome}, qual seu salário?'))
print('Legal')
emprestimo = float(input('Qual o valor necessário para a compra da casa?'))
meses = int(input('Em quantos meses deseja pagar?'))
mensal = emprestimo/meses
print(f'A mensalidade será de R${mensal}')
if mensal >= salario*0.30:
    print('Empréstimo negado, o valor do empréstimo não pode exceder a 30% do seu salario!')
else:
    print('Parabéns, empréstimo aprovado!')