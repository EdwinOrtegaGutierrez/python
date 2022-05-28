from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.button import Button

class Edwin(App):

    def build(self):
        # Cuando no se envian parametros -> return super().build()
        # Texto en pantalla -> return Label(text = 'Texto en pantalla')
        boton  = Button(text='Boton', font_size=40, size_hint=(0.3, 0.1), pos=(250, 400), background_color=("tomato"))

        return boton

if __name__ == '__main__':
    Edwin().run()