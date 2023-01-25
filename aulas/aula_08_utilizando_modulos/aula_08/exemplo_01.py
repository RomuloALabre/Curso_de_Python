import math
# ou você pode importar apenas algo específico, para economizar memória
from math import sqrt
from math import ceil

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')