shopping_bag = {}
def buy(shopping_bag):
    print('[구입]')
    item = input('상품명?')
    if item == '':
        return False
    c = int(input('수량은?'))
    print(f'장바구니에 {item} {c}개 담겼습니다.')
    shopping_bag[item] = c
def show(shopping_bag):
    print(f'>>> 장바구니 보기:{shopping_bag}')
def find(shopping_bag):
    print('[검색]')
    sr = input('장바구니에서 확인하고자 하는 상품은?')
    if shopping_bag.get(sr) == None:
        return print(f'{sr}은(는) 장바구니에 존재하지 않는 상품입니다.')
    print(f'{sr}은(는) {shopping_bag[sr]}개 담겨 있습니다.')
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)

