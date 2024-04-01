int_list = [ ]

while True:
    val = int(input("정수를 입력하시오: "))
    int_list.append(val)
    if val == 0:
        break

sum = 0
i = 0
while True:
    sum = sum + int_list[i]
    i = i + 1
    if int_list[i] == 0:
        break

print(sum)