from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
# from kivy.uix.boxlayout import BoxLayout


class FunkyButtonWidget(ButtonBehavior, AnchorLayout):
    txtInput = StringProperty("")
    btnTxt = StringProperty("1")

    def on_button_click(self):
        self.txtInput += str(self.btnTxt)


class ButtonClickExample(App):
    pass;


ButtonClickExample().run()
