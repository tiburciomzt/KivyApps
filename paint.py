from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from random import random


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):     #Funcion MotionEvent(toque,clic,etc)
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color)
            d = 30
            Ellipse(pos=(touch.x -d /2, touch.y -d/2)),
            size=(d,d)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]