product = "coffee"
count = 3
price = 1500.5

print(f"상품 {product} {count}개의 가격은 {(count*price):.3f}원입니다.")
print("상품 %s %d개의 가격은 %.3f원입니다." %(product, count, count*price))