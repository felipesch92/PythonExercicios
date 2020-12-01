d = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
v_d = d * 60
v_km = km * 0.15
v = v_d + v_km
print('Valor pelos dias é de R$ {:.2f}, o valor por km rodado é de R$ {:.2f} o total a pagar é de R$ {:.2f}'.format(v_d, v_km, v))
