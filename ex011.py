lar = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = lar*alt
tinta = area/2
print('Área total de: {:.3f}, será necessário {:.3f} litro(s) de tinta.'.format(area, tinta))
