from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from random import randint

Window.size = (300, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "androidTest1"

class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text='Converter')
        self.miles = Label(text='Miles')
        self.metres = Label(text='Metres')
        self.centimetres = Label(text='Centimetres')
        self.input_data = TextInput(hint_text='Enter value in kilometres', multiline = False)
        self.input_data.bind(text = self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.miles.text = 'Miles: ' + str(float(data) * 0.62)
            self.metres.text = 'Metres: ' + str(float(data) * 1000)
            self.centimetres.text = 'Centimetres: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''

    def btn_pressed(self, instance):
        self.label.color = (randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1)

    def build(self):
        box = BoxLayout(orientation = 'vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.metres)
        box.add_widget(self.centimetres)

        return box

if __name__ == "__main__":
    MyApp().run()
