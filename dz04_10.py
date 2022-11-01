# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

#from re import X

print(my_favorite_songs[:14],  end='   ' )
#print(my_favorite_songs.find('N'))
#print(my_favorite_songs[64:], end=' ')
print(my_favorite_songs[-13:], end='   ')
print(my_favorite_songs[16:30], end = '   ')
#print(my_favorite_songs[51:62])
print(my_favorite_songs[51:-15])