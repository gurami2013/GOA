temperature = [72, 68, 75, 70, 78, 74, 71]
print(temperature)
max(temperature)
min(temperature)
avrage = sum(temperature) / len(temperature)


above_70 = []

for i in temperature:
    if i>70:
        above_70.append(i)
print(above_70)        
