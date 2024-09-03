from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class FirstAppWidget(Widget):
    pass


class LoginPage(AnchorLayout):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1, 101):
            btn = Button(text="Button {0}".format(i), size_hint=(None, None), size=(dp(200), dp(200)), pos_hint={
                'center_x': 0.5, 0.5: dp(200), 'center_y': 0.5})
            self.add_widget(btn)


class GridLayoutExample(GridLayout):
    pass


class FirstApp(App):
    pass


if __name__ == '__main__':
    FirstApp().run()
