spisok = [1,2,3,4,5,6,7]
i = int(input())
print("i-й элемент ряда:",spisok[i])
print("Список из i элементов равных i:", [spisok[i] for j in range(i)])