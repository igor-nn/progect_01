# сортировка
from random import randint, random

mas = []
x = 10
while x > 0:
    mas.append(randint(10,100))
    x-=1
print('сгенерированный массив:',mas)

    # --------сортировка выбором

x = 10
i = 0
while i < x - 1:
  m = i
  j = i + 1
  while j < x:
    if mas [j] < mas [m]:
      m = j
    j += 1
  mas [i], mas [m] = mas [m], mas [i]
  i += 1

print('Сортировка выбором:',mas)

# ------------сортировка пузырьком (реверс)

n = len(mas)
for i in range(n-1):
  for j in range(n-i-1):
   if mas[j] < mas[j+1]:
     mas[j], mas[j+1] = mas[j+1], mas[j]
print ('Сортировка пузырьком (реверс):',mas)



