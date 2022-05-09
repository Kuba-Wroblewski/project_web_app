
# lista = ['$16.51', '$16.51', '$27.00', '$27.00']
lista = ['$16.51']
print('Orgin >>', lista)

f_list = [entry.replace('$', '') for entry in lista]
print('Minus "$" >>', f_list)

lista_cen = 0
for i in range(len(f_list)):
    f_list[i] = float(f_list[i])
    print('Element in list >>', f_list[i])
    lista_cen += f_list[i]
print('Suma all price >>', lista_cen)
lista_cen = int(lista_cen/0.01)/100

print(type(lista_cen), lista_cen)
# lista_cen = str(lista_cen)


lista_cen = lista_cen * 10
lista_cen = round(lista_cen, 2)
print(lista_cen)



