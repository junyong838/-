import pickle
import os

filepath = 'score.bin'
List = []
t = ''
def input_scores(num):
    if 0 <= num <= 100:
        List.append(num)
        return True
    else:
        return False
def get_average():
    total = 0
    for i in List:
        total += i
    return total / len(List)
def show_scores():
    print('[점수 출력]')
    print(f'개인점수: {List}')
    print(f'평균: {t}')

if not(os.path.exists(filepath)):
    i = 1
    print('[점수 입력]')
    while True:
        num = int(input(f'#{i}?'))
        i += 1
        if input_scores(num):
            pass
        else:
            break

    t = get_average()

    with open(filepath, 'wb') as file:
        pickle.dump(List, file)
        pickle.dump(t, file)
    
    show_scores()
else:
    print('[파일 읽기]')
    with open(filepath, 'rb') as file:
        List = pickle.load(file)
        t = pickle.load(file)
        show_scores()