listaPrecos = [ 1500, 1000, 800, 3000]

#imposto
#aliquota1 - IR = 0.2 se o preço do produto for até R$ 2000. Acima disso a aliquota é 0.3
#aliquota1 - ISS = 0.15
#aliquota1 - CSLL = 0.5


def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total
    

for preco in listaPrecos:
    imposto_total = calcula_imposto_total(preco)
    print(f'Imposto total sobre o produto de R${preco}: R${imposto_total}')


nova_lista_produtos = [4000, 5000, 6000, 7000]

for preco in nova_lista_produtos:
    imposto_total = calcula_imposto_total(preco)
    print(f'Imposto total sobre o produto de R${preco}: R${imposto_total}')