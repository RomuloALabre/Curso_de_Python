lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:
    print(f'Eu comi {comida}')
print('Comi Bastanteee')
print(len(lanche))

print('#'*9)
for comida in range(0, len(lanche)):
    print(f'Eu comi {lanche[comida]}')

print('#'*9)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')