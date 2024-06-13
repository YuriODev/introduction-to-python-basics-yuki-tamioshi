n = int(input('enter a 4 digit no.'))
d1 = n // 1000 
d2 = (n % 1000) // 100
d3 = (n % 100) // 10
d4 = n % 10 
if d1 == d4 and d2 == d3:
  print('1')
else:
  print('0')
