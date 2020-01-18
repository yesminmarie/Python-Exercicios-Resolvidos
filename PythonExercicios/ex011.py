largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura*altura
# um litro de tinta pinta 2m²
tinta = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Serão necessários {:.2f} l de tinta para pintar a parede'.format(tinta))
