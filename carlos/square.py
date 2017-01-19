import turtle
from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self,height,length):
        super(Square,self).__init__(height,height)
    def set_height(self,height):
        super(Square,self).set_height(height)
        new_length=self.height
        new_height=self.height
    def get_area(self):
        return self.length*self.height
    def draw_shape(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.pendown()
        self.turtle.goto(self.length,0)
        self.turtle.goto(self.length,self.height)
        self.turtle.goto(0,self.height)
        self.turtle.goto(0,0)
        self.turtle.penup()
        self.has_been_drawn=True        
