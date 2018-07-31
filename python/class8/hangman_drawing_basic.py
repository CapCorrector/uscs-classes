import turtle

class HangmanDrawer:
    def __init__(self):
        self.pen = turtle.Pen()
        self.pen.hideturtle()
        self.current_step = 0

    def next(self):
        if self.current_step == 0:
            self.draw_frame()
        elif self.current_step == 1:
            self.draw_hang_line()
        elif self.current_step == 2:
            self.draw_head()
        elif self.current_step == 3:
            self.draw_one_arm()
        elif self.current_step == 4:
            self.draw_another_arm()
        elif self.current_step == 5:
            self.draw_body()
        elif self.current_step == 6:
            self.draw_one_leg()
        elif self.current_step == 7:
            self.draw_another_leg()
            self.draw_text()
            return False

        self.current_step += 1
        return True
        
    def draw_frame(self):
        self.pen.up()
        self.pen.setposition(-100, 0)
        self.pen.down()
        self.pen.setposition(100, 0)
        self.pen.setposition(100, 20)
        self.pen.setposition(-100, 20)
        self.pen.setposition(-100, 0)        
        self.pen.up()
        self.pen.setposition(100, 20)
        self.pen.down()
        self.pen.setposition(30, 300)
        self.pen.setposition(-10, 300)

    def draw_hang_line(self):
        self.pen.setposition(-10, 250)

    def draw_head(self):
        self.pen.left(180)
        self.pen.circle(15)

    def draw_one_arm(self):
        self.pen.up()
        self.pen.setposition(-10, 220)
        self.pen.down()
        self.pen.setposition(-60, 200)

    def draw_another_arm(self):
        self.pen.up()
        self.pen.setposition(-10, 220)
        self.pen.down()
        self.pen.setposition(40, 200)

    def draw_body(self):
        self.pen.up()
        self.pen.setposition(-10, 220)
        self.pen.down()
        self.pen.setposition(-10, 170)

    def draw_one_leg(self):
        self.pen.setposition(-30, 100)

    def draw_another_leg(self):
        self.pen.up()
        self.pen.setposition(-10, 170)
        self.pen.down()
        self.pen.setposition(10, 100)

    def draw_text(self):
        self.pen.up()
        self.pen.setposition(0, -50)
        self.pen.write('You lose!', align='center', font=('Arial', 24, 'normal'))

if __name__ == '__main__':
    drawer = HangmanDrawer()
    drawer.draw_frame()
    drawer.draw_hang_line()
    drawer.draw_head()
    drawer.draw_one_arm()
    drawer.draw_another_arm()
    drawer.draw_body()
    drawer.draw_one_leg()
    drawer.draw_another_leg()
    drawer.draw_text()
