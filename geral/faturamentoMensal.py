# Definindo estados
sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
out = float(19.84953)
total = float(sp + rj + mg + es + out)

# Calculo da Porcentagem
psp = ((sp/total)*100)
prj = ((rj/total)*100)
pmg = ((mg/total)*100)
pes = ((es/total)*100)
pout = ((out/total)*100)

print('Porcentagem de São Paulo {}%'.format(psp))
print('Porcentagem de Rio de Janeiro {}%'.format(prj))
print('Porcentagem de Minas Gerais {}%'.format(pmg))
print('Porcentagem de Espirito Santo {}%'.format(pes))
print('Porcentagem referente aos outros valores {}%'.format(pout))