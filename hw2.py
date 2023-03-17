def get_integer(prompt):
    return int(input(prompt))

def exchange(coin):
    fhw = coin // 500
    r = coin % 500
    hw = r // 100
    r %= 100
    fw = r // 50
    r %= 50
    w = r // 10
    print("500원 동전의 개수:", fhw)
    print("100원 동전의 개수:", hw) 
    print("50원 동전의 개수:", fw) 
    print("10원 동전의 개수:", w) 
coin = get_integer("동전으로 교환하고자 하는 금액은?")
exchange(coin)