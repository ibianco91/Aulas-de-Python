"""Conversor de Unidades"""
import math
base = int(input('Digite o item que você deseja converter:[1] Moeda\n[2] Comprimento\n[3] Área\n[4] Volume\n[5] Velocidade\n[6] Massa\n[7]Pressão\n[8] Moeda\n[9] Temperatura\nOpção:'))
valor = float(input('Digite o valor a ser convertido: '))
unidade.inicial = str(input('Digite a unidade inicial: ')).lower().strip()
while true:
    if base == 9:
        if unidade.inicial=='c':
            print('Fahrenheit =  {:.3}F\nKelvin = {:.3}K' .format(9*valor/5+32, valor+273.15))
        elif unidade.inicial=='f':
            print('Celsius =  {:.3}C\nKelvin = {:.3}K' .format((valor-32)*5/9, (valor-32)*5/9+273.15)
        else:
            print('Celsius =  {:.3}C\nFahrenheit = {:.3}F' .format(valor-273.15, (valor-273.15)*9/5+32)


