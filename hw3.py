I = int(input("활인율은? "))
A = int(input("A 상품의 활인된 가격은? "))
B = int(input("B 상품의 활인된 가격은? "))

def get_fixed_price(price, sale):
    return int(price / (1 - sale/100)) 
print("A 상품의 정가는 {0} 원".format(get_fixed_price(A,I)))
print("B 상품의 정가는 {0} 원".format(get_fixed_price(B,I)))