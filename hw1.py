def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area(r):
    return 3.14*r*r
prompt = "넓이를 구하고자 하는 원의 반지름은?"
r = get_radius(prompt)
a = get_circle_area(r)
print("반지름 {0}인 원의 넓이 = 3.14 x {0} x {0} = {1}".format(r, a))