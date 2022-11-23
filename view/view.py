from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

class Manager(ScreenManager):
    pass

class View(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        Builder.load_file("view/ui.kv")
        return Manager()

