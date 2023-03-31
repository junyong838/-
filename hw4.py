def rep_char(c, n):
    print(c * n)
def draw_string(k):
    H = 'Hello {0},'.format(k)
    W = "Welcome to Seoul."
    nstr = len(H) if ((len(H)) > len(W)) else len(W)
    rep_char('-', nstr)
    print(H)
    print(W)
    rep_char('-', nstr)
w = input('Input his/her name:')
draw_string(w)
