def read_single_digit(num):
    if num == '1': return '일 '
    elif num == '2': return '이 '
    elif num == '3': return '삼 '
    elif num == '4': return '사 '   
    elif num == '5': return '오 '
    elif num == '6': return '육 '
    elif num == '7': return '칠 '
    elif num == '8': return '팔 '
    elif num == '9': return '구 '
    elif num == '0': return '영 '
    else: return ""
def read_number(num):
    return read_single_digit(num[:1]) + read_single_digit(num[1:2]) + read_single_digit(num[2:])

num = input("세 자리 정수 입력: ")
print(read_number(num))