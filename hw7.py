
shopping_bag = {}
print('[구입]')
while True:
    item = input('상품명?')
    if item == '':
        break
    c = int(input('수량은?'))
    shopping_bag[item] = c
    print(f'장바구니에 {item}이(가) 담겼습니다.')
print(f'>>> 장바구니 보기:{shopping_bag}')
print('[검색]')
sr = input('장바구니에서 확인하고자 하는 상품은?')
print(f'{sr}은(는) {shopping_bag[sr]}개 담겨 있습니다.')