numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

a = []
sum = 0
for i in range(0,len(numbers)):
    if numbers[i] is not None:
        sum+= numbers[i]

for i in range(0, len(numbers)):
    if numbers[i] is not None:
        a.append(numbers[i])
    else: a.append(round(sum/(len(numbers)-1), 2))


print("Измененный список:", a)
