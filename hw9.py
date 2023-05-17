class point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.list = (x ,y)        
    def show(self):
        return self.list
    def set(self, x, y):
        self.x = x
        self.y = y
    def get(self):
        self.list = tuple(self.list)
        self.x = self.list[0]
        self.y = self.list[1]
        return self.x , self.y
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = point(x1, y1)
        self.rb = point(x2, y2)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def show(self):
        print(f'좌측 상단 꼭지점이 {self.lt.show()}이고 우측 상단 꼭지점이 {self.rb.show()}인 사각형입니다.', end='')    
    def getWidth(self):
        self.width = self.x2 - self.x1
    def getHeight(self):
        self.height = self.y2 - self.y1
    def getArea(self):
        self.getWidth()
        self.getHeight()
        self.area = self.height * self.width
        return self.area
    def getPerimeter(self):
        self.getWidth()
        self.getHeight()
        self.perimeter = self.width * 2 + self.height * 2
        return self.perimeter
# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')