import random
number = random.randint(0, 99)
selectnum = print(input("복권번호를 입력하시오(0에서 99 사이): "))
price = 0

print("당첨 번호는 " + str(number) + "입니다.")

if (number % 10) == (selectnum % 10):
    price = price + 50

if (number // 10) == (selectnum // 10):
    price = price + 50

if price == 0:
    print("상금이 없습니다.")
else :
    print("상금은 " + str(price) + "만원입니다.")