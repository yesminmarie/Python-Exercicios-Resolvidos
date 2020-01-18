salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    print('O novo salário será {:.2f}'.format(salario+salario*0.1))
else:
    print('O novo salário será {:.2f}'.format(salario+salario*0.15))