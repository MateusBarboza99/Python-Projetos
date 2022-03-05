valor = float(input('Quantos Pretende Guardar?:R$'))
mes = int(input('Durante quantos Mês? : '))
ano = valor * mes
print('Com valor de R${:.2f} Reais durante {:.0f} mesês você tera quardado R${:.2f} Reais'.format(valor, mes, ano))
