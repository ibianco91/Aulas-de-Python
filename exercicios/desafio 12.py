v=float(input('qual o valor do produto?'))
d=float(input('qual o desconto do produto?'))
print('com {}% de desconto ele sai de {} por {:.2}' .format(d,v,(v-(v*d/100))))