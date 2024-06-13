num = int(input('enter a 4 digit no.'))
d1 = num // 1000
d2 = (num % 1000) // 100
d3 = (num % 100) // 10
d4 = num % 10
sum = d1 + d2 + d3 + d4
print(sum)
