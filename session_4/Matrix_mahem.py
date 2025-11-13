import random

row1 = [random.randint(1,9),random.randint(1,9),random.randint(1,9)]
row2 = [random.randint(1,9),random.randint(1,9),random.randint(1,9)]
row3 = [random.randint(1,9),random.randint(1,9),random.randint(1,9)]

matrix = [row1,row2,row3]

for row in matrix:
    print(row)

print(f"sum of row 1 is {row1[0] + row1[1] + row1[2]}")
print(f"sum of row 2 is {row2[0] + row2[1] + row2[2]}")
print(f"sum of row 3 is {row3[0] + row3[1] + row3[2]}")

print(f"sum of column 1 is {row1[0] + row2[0] + row3[0]}")
print(f"sum of column 2 is {row1[1] + row2[1] + row3[1]}")
print(f"sum of column 3 is {row1[2] + row2[2] + row3[2]}")