a = int(input('enter first digit'))
b = int(input('enter second digit'))
c = int(input('enter third digit'))
mini = ((a + b) - abs(a - b)) // 2
max = ((a + b) + abs(a - b)) // 2
mid = (a + b + c) - mini - max
print(mini,mid,max)
