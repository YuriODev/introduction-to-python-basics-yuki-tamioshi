h =  int(input())
min = int(input())
sec = int(input())
tsec = (h * 3600) + (min * 60) + sec
H_angle = (tsec / 3600)*360
print(H_angle)
