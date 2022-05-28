from kivy.core.window import Window
from kivy.app import App
from kivy.uix.image import Image

class ImagenApp(App):
    def build(self):
        Window.size = (600, 600)
        return Image(source='astronauta.png')

if __name__ == '__main__':
    ImagenApp().run()