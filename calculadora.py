from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Calculadora(BoxLayout):
    
    def run(self):
        root = BoxLayout(orientation='vertical')
        label = Label(size_hint_y=1)

        buttons = ('1', '2','3', '+',
        '4', '5','6', '-',
        '7', '8','9', '.',
        '0', '*','/', '=',
        )

        button_grid = GridLayout(cols=4, size_hint_y=2)

        for digit in buttons:
            button_grid.add_widget(Button(text=digit))

        clear = Button(text='clear', size_hint_y = None, height=100)

        root.add_widget(label)
        root.add_widget(button_grid)
        root.add_widget(clear)

        return root
