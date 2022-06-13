n = input('Введите число n:')
n1 = int(n)
n2 = int(f'{n}{n}')
n3 = int(f'{n}{n}{n}')
result = n1+n2+n3
print(f'n+nn+nnn={n1}+{n2}+{n3}={result}')