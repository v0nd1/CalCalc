from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CalCalcApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, CalCalc", halign="center")


CalCalcApp().run()