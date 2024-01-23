name = input('Enter name of product:')
a = int(input('Enter prize: ')) 
b = int(input('Enter number of product: '))
payment = a * b


header = '-' * 9 + 'Receipt' + '-' * 9
print(header)
print('Product name:', f'{name:>11}')
print('Prize:', f'{a:>18}')
print('Number:', f'{b:>17}')
print('Payment:', f'{payment:>16}')