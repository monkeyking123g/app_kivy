from tracemalloc import start
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
#Window.size = (720, 1280)
Window.size = (480, 853)

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

def get_ingridients(m):
    nitro = str(10 * m / 1000)
    sait = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    dexstrose = str(5 * m / 1000)
    saliting_time = str(round(m / 500 * 2))

    return {'nitro': nitro, 'sait': sait, 'starts':starts, 'dexstrose': dexstrose,  'saliting_time': saliting_time}

class Container(GridLayout):

    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingredients = get_ingridients(mass)
        self.salt.text = ingredients.get('sait') + ' + 5'
        self.nitro.text = ingredients.get('nitro')
        self.sugars.text = ingredients.get('dexstrose')
        self.starts.text = ingredients.get('starts')
        self.time.text = ingredients.get('saliting_time') 

class MyApp(App):
    
    def build(self):
       
        return Container()


if __name__ == '__main__':
    MyApp().run()

