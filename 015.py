import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Rectangle:
    def __init__(self, x_1, x_2, y_1, y_2):
        self.x_1 = x_1
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2

    def width(self):
        width = abs(self.x_1 - self.x_2)
        return width

    def height(self):
        height = abs(self.y_1 - self.y_2)
        return height

    def area(self):
        w = self.width()
        h = self.height()
        area = w*h
        return area

    def circumference(self):
        w = self.width()
        h = self.height()
        cf = 2*w + 2*h
        return cf


class Square(Rectangle):
    def __init__(self, x_1, y_1, l):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_1 + l
        self.y_2 = y_1 + l

    def len(self):
        len_1 = self.width()
        return len_1


def r_s():
    while 1:
        rs = input("Press 'S' for Square, press 'R' for Rectangle: ")
        if rs == 'S' or rs == 's' or rs == 'R' or rs == 'r':
            print("若想得到图形请将边长控制在0.5以内")
            return rs
        else:
            print("Input the 'S' or 'R' please!")


def r_input():
    print("Please input Diagonal's coordinates of Rectangle")
    while 1:
        while 1:
            try:
                x__1 = float(input("x_1; "))
                y__1 = float(input("y_1; "))
                x__2 = float(input("x_2; "))
                y__2 = float(input("y_2; "))
            except ValueError:
                print("Input the number please!")
            else:
                x_1 = x__1
                x_2 = x__2
                y_1 = y__1
                y_2 = y__2
                break
        if x_1 == x_2 or y_1 == y_2:
            print("It's not a Rectangle")
        else:
            break
    global r
    r = Rectangle(x_1, x_2, y_1, y_2)
    r_calculate(r)


def s_input():
    print("Please input len and any coordinates of apex angle of Square")
    while 1:
        try:
            x__1 = float(input("x_1; "))
            y__1 = float(input("y_1; "))
            while 1:
                len_1 = float(input("len: "))
                if len_1 <= 0:
                    print("Input the len greater that zero please!")
                else:
                    break
        except ValueError:
            print("Input the number please!")
        else:
            x_1 = x__1
            y_1 = y__1
            break
    l = len_1
    global s
    s = Square(x_1, y_1, l)
    s_calculate(s)


def r_calculate(r_c):
    rw = r_c.width()
    rh = r_c.height()
    ra = r_c.area()
    rc = r_c.circumference()
    return rw, rh, ra, rc


def s_calculate(s_c):
    sl = s_c.len()
    sa = s_c.area()
    sc = s_c.circumference()
    return sl, sa, sc


def output(o, rs):
    if rs == 'S' or rs == 's':
        sl, sa, sc = s_calculate(o)
        print("Len:", sl)
        print("Area:", sa)
        print("Circumference:", sc)
        if sl <= 0.5:
            shape(s.x_1, s.x_2, s.len(), s.len())
    elif rs == 'R' or rs == 'r':
        rw, rh, ra, rc = r_calculate(o)
        print("Width:", rw)
        print("Height:", rh)
        print("Area:", ra)
        print("Circumference:", rc)
        if (rw <= 0.5) and (rh <= 0.5):
            shape(min(r.x_1, r.x_2), min(r.y_1, r.y_2), r.width(), r.height())


def shape(x, y, w, h):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.add_patch(patches.Rectangle((x, y), w, h))
    plt.show()


def main():
    rs = r_s()
    if rs == 'S' or rs == 's':
        print("Calculating S......")
        s_input()
        output(s, rs)
    elif rs == 'R' or rs == 'r':
        print("Calculating R......")
        r_input()
        output(r, rs)


def brk():
    while 1:
        global gn
        gn = input("Again?(type 'Yes' or 'Not'):")
        if gn == 'Yes' or gn == 'Not'or gn == 'yes' or gn == 'not':
            break
        else:
            print("Type 'Yes' or 'Not' please!")


if __name__ == "__main__":
    while 1:
        main()
        brk()
        if gn == 'Not' or gn == 'not':
            print("End.")
            break
