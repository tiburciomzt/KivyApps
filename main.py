from kivy.app import App
from paint import MyPaintWidget
from calculadora import Calculadora


class MyPaintApp(App):
    def build(self):
        calculadora_app = Calculadora()
        return calculadora_app.run()


if __name__=="__main__":
    app = MyPaintApp()
    app.run()