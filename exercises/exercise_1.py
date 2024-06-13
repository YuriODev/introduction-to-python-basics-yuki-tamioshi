num=int(input('enter a five digit no.'))
d5=num%10
num//=10
d4=num%10
num//=10
d3=num%10
num//=10
d2=num%10
num//=10
d1=num%10
num//=10
sum1 = d1 + d3 + d5
sum2 = d2 + d4
new_num = sum1 * 10 + sum2 
print('the new number is:',new_num)
