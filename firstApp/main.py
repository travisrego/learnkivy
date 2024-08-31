from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class AnchorLayoutExample(AnchorLayout):
    pass


class FirstAppWidget(Widget):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class FirstApp(App):
    pass


if __name__ == '__main__':
    FirstApp().run()
