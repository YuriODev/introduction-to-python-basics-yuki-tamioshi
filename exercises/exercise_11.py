a = int(input())
bills = [500, 100, 50, 10, 5, 2, 1]
for i in bills:
  price = a//i
  print(price, i)
  a %= i
