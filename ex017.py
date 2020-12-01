from math import pow, sqrt, hypot
cat_o = float(input('Digite o comprimento do cateto oposto: '))
cat_a = float(input('Digite o comprimento do cateto adjacente: '))
c_hip = pow(cat_o, 2) + pow(cat_a, 2)
c_hip_final = sqrt(c_hip)
print('O comprimento da hipotenusa é de: {:.2f}'.format(c_hip_final))
print('O comprimento da hipotenusa é de {:.2f}'. format(hypot(cat_o, cat_a)))
