n = int(input('enter the No. in sec'))

h = n // 3600
min = (n % 3600) // 60
sec = (n % 3600) % 60 
print(f'{h}:{min:02}:{sec:02}')
