radius = int(input("반지름을 입력하시오: "))
# area = 3.141592 * radius * radius
# area = 3.141592 * radius **2
area = 3.141592 * pow(radius,2) # [파이썬제곱연산함수pow()와연산자**의차이] 있음
print("반지름이", radius, "인 원의 넓이 =", area)